# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.db.models import Avg, Count
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout as auth_logout, get_user_model
from django.template import RequestContext
from django.db import transaction


import xml.etree.ElementTree as ET
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from activitytree.models import Course,ActivityTree,UserLearningActivity, LearningActivity, ULA_Event, FacebookSession,LearningActivityRating
from activitytree.interaction_handler import SimpleSequencing
from activitytree.interaction_handler import get_nav

from activitytree.activities import activities, multi_device_activities

from mongo_activities import Activity

import urllib
import urlparse

from eval_code.RedisCola import Cola, Task
import json
from django.conf import settings


import redis

ip_couch = "http://10.10.184.236:5984"
redis_service = redis.Redis("127.0.0.1")


def welcome(request):
    # plus_scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    # plus_id=settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY
    courses = Course.objects.all()

    if request.user.is_authenticated() and request.user != 'AnonymousUser' :
         return render_to_response('activitytree/welcome.html',
            {'courses':courses
                #, 'plus_scope':plus_scope,'plus_id':plus_id
            },
                context_instance=RequestContext(request))
    else:
        return render_to_response('activitytree/welcome.html',
            {'user_name':None,'courses':courses
                #,'plus_scope':plus_scope,'plus_id':plus_id
                 },
                context_instance=RequestContext(request))

def dashboard(request,path_id):
    if request.user.is_authenticated():
        if request.method == 'GET':

            s = SimpleSequencing()

            # First, the requested_activity  exists??
            # Gets the Learning Activity object from uri
            requested_activity = None
            try:
                requested_activity = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user )
            except (ObjectDoesNotExist, IndexError) as e:
                requested_activity = None


            if not requested_activity:
                return HttpResponseNotFound('<h1>Activity not found</h1>')

            # Gets the root of the User Learning Activity
            root = UserLearningActivity.objects.get(learning_activity_id = path_id ,user = request.user )

                # Exits last activity, and sets requested activity as current
                # if choice_exit consider complete


            _XML = get_nav(root)
            #Escape for javascript
            XML=ET.tostring(_XML,'utf-8').replace('"', r'\"')        #navegation_tree = s.nav_to_html(nav)

            return render_to_response('activitytree/dashboard.html', {'XML_NAV':XML,
                                    'children': requested_activity.get_children(),
                                    'uri':requested_activity.learning_activity.uri,
                                    'root':requested_activity.learning_activity.get_root().uri,
                                    'root':requested_activity.learning_activity.get_root().uri
                                                                    },
                                      context_instance=RequestContext(request))


def path_activity(request,path_id, uri):
    learning_activity = None
    try:
        learning_activity = LearningActivity.objects.get(pk=path_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Learning Activity not found</h1>')

    if request.user.is_authenticated():
        root=None
        s = SimpleSequencing()
        requested_activity = None

        if request.method == 'GET':
            try:
                requested_activity = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user )
            except (ObjectDoesNotExist, IndexError) as e:
                requested_activity = None

            print requested_activity


            # The requested_activity was NOT FOUND
            if not requested_activity: # The requested_activity was not found
            # Maybe a
            # 'start' REQUEST?
            #    if 'nav' in request.GET and request.GET['nav'] == 'start':
                if learning_activity and learning_activity.root is None:
                    s.assignActivityTree(request.user,learning_activity)
                    requested_activity = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user)
                    _set_current(request,requested_activity, requested_activity, s)
                    return HttpResponseRedirect( '/%s%s'% (path_id , uri))
                #If is not a root learning activity then sorry, not found
                else:
                    return HttpResponseNotFound('<h1>Activity not found</h1>')
            #Else NOT FOUND
                #else:
                #    return HttpResponseNotFound('<h1>Activity not found</h1>')

            # We have a valid requested_activity, lets handle OTHER NAVIGATION REQUEST

            #Get root of activity tree
            root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root(),
                                                       user = request.user )[0]
            # 'continue' REQUEST?
            if requested_activity.is_root() and 'nav' in request.GET and request.GET['nav'] == 'continue':
                current_activity = s.get_current(requested_activity)
                if current_activity:
                    requested_activity = current_activity
                    return HttpResponseRedirect(  '/%s%s'% requested_activity.learning_activity.id,requested_activity.learning_activity.uri)
                else:
                    _set_current(request,requested_activity, root, s, objective_status=None, progress_status=None)
            #Else is a
            # 'choice' REQUEST
            else:
                _set_current(request,requested_activity, root, s)

        if request.method == 'POST' and 'nav_event' in request.POST:
            #Get root of activity tree
            root = None
            try:
                root = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user )
            except (ObjectDoesNotExist, IndexError) as e:
                root = None


            if not root or not root.is_root():
                return HttpResponseNotFound('<h1>Activity not found</h1>')

            current_activity = s.get_current(root)


            if current_activity.learning_activity.is_container:
                progress_status = None
                objective_status = None
            else:
                ###
                ###  What if status in POST??
                ###
                progress_status = 'complete'
                objective_status = 'satisfied'

            # 'next' REQUEST
            if request.POST['nav_event'] == 'next':
                # Go TO NEXT ACTIVITY
                s.exit( current_activity, progress_status = progress_status, objective_status = objective_status)
                next_uri = s.get_next(root, current_activity)

            # 'prev' REQUEST
            elif request.POST['nav_event'] == 'prev':
                # Go TO PREV ACTIVITY
                s.exit( current_activity, progress_status = progress_status, objective_status = objective_status)
                next_uri = s.get_prev(root, current_activity)

            print next_uri
            #No more activities ?
            if next_uri is None:

                return HttpResponseRedirect( '/%s%s'% (root.learning_activity.id , root.learning_activity.uri))

            else:
                next_activity = UserLearningActivity.objects.get(learning_activity__id = next_uri ,user = request.user )
                return HttpResponseRedirect( '/%s%s'% (next_activity.learning_activity.id,next_activity.learning_activity.uri))


        _XML = get_nav(root)
        #Escape for javascript
        XML=ET.tostring(_XML,'utf-8').replace('"', r'\"')

        breadcrumbs = s.get_current_path(requested_activity)
        print "uri",requested_activity.learning_activity.uri
        activity_content = Activity.get(requested_activity.learning_activity.uri)
        print 'activity:', activity_content

        if activity_content and 'content' in activity_content:
            content = activity_content['content']
        else:
            content = ""

        update_pool(requested_activity.learning_activity.uri)
        print activity_content,uri
        if (requested_activity.learning_activity.uri).split('/')[2] =='video':
            return render_to_response('activitytree/video.html',

                                  {'XML_NAV':XML,
                                   'uri':requested_activity.learning_activity.uri,
                                   'uri_id':requested_activity.learning_activity.id,
                                   'video':activity_content,
                                   'breadcrumbs':breadcrumbs,
                                   'root':requested_activity.learning_activity.get_root().uri,
                                   'root_id':'/%s'% requested_activity.learning_activity.get_root().id},
                                    context_instance=RequestContext(request))

        elif requested_activity.learning_activity.is_container:

            return render_to_response('activitytree/container.html',

                                  {
                                   'XML_NAV':XML,
                                   'children': requested_activity.get_children(),
                                   'uri':requested_activity.learning_activity.uri,
                                   'uri_id':'/%s'% requested_activity.learning_activity.id,
                                   'content':content,
                                   'root':requested_activity.learning_activity.get_root().uri,
                                   'root_id':'/%s'% requested_activity.learning_activity.get_root().id,
                                   'breadcrumbs':breadcrumbs},
                                    context_instance=RequestContext(request))
        else:
            return render_to_response('activitytree/activity.html',

                                  {'XML_NAV':XML,
                                   'uri':requested_activity.learning_activity.uri,
                                   'uri_id':'/%s'% requested_activity.learning_activity.id,
                                   'content':content,
                                   'root':requested_activity.learning_activity.get_root().uri,
                                   'root_id':'/%s'% requested_activity.learning_activity.get_root().id,
                                   'breadcrumbs':breadcrumbs},
                                    context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)



def activity(request, uri=None):
    if request.method == 'GET':

        # Check if public, all public for now
        if False:
            return HttpResponseRedirect('/login/?next=%s' % request.path)
        print '/%s' % uri
        activity_content = Activity.get('/%s' % uri)

        if activity_content and 'content' in activity_content:
            content = activity_content['content']
        else:
            content = ""


        if (uri).split('/')[1] =='video':
            print activity_content
            return render_to_response('activitytree/video.html',

                                  {'XML_NAV':None,
                                   'uri':uri,
                                   'video':activity_content,
                                   'breadcrumbs':None },
                                    context_instance=RequestContext(request))


        else:
            return render_to_response('activitytree/activity.html',

                                  {'XML_NAV':None,
                                   'uri':uri,
                                   'content':content,
                                   'breadcrumbs':None,
                                   },
                                    context_instance=RequestContext(request))


        # Do something for anonymous users.    

def path_test(request,path_id, uri):

    if request.user.is_authenticated():
        s = SimpleSequencing()
        try:
            requested_activity = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user )
        except ObjectDoesNotExist as e:
            return HttpResponseNotFound('<h1>Learning Activity not found</h1>')

        root = None

        try:
            root = UserLearningActivity.objects.get(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )
        except (ObjectDoesNotExist, IndexError) as e:
                return HttpResponseNotFound('<h1>Path not found</h1>')

        feedback = None
        attempts_left = requested_activity.learning_activity.attempt_limit-requested_activity.num_attempts
        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            # if choice_exit consider complete
            _set_current(request,requested_activity, root, s, objective_status=None, progress_status=None)

        elif request.method == 'POST':
            if 'check' in request.POST and attempts_left :

                    #quiz = activities[requested_activity.learning_activity.uri]
                    quiz = Activity.get(requested_activity.learning_activity.uri)

                    feedback = _check_quiz(request.POST, quiz)
                    # Updates the current Learning Activity
                    objective_measure = float(feedback['total_correct'])/len(quiz['questions'])*100
                    if feedback['total_correct'] >= quiz['satisfied_at_least']:
                        objective_status='satisfied'
                    else:
                        objective_status='notSatisfied'

                    s.update(requested_activity, objective_status = objective_status, objective_measure = objective_measure,attempt=True)
                    attempts_left-=1


       # Gets the current navegation tree as HTML

        _XML = get_nav(root)
        #Escape for javascript
        XML=ET.tostring(_XML,'utf-8').replace('"', r'\"')        #navegation_tree = s.nav_to_html(nav)

        breadcrumbs = s.get_current_path(requested_activity)



        test = Activity.get(requested_activity.learning_activity.uri)

        if feedback:
            for q in test['questions']:
                if q['id'] in feedback:
                    q['feedback'] = feedback[q['id']]
                    if q['interaction']  in ['choiceInteraction','simpleChoice']:
                        q['feedback_options'] = zip(q['options'], feedback[q['id']]['user_answer'], feedback[q['id']]['checked'])

        return render_to_response('activitytree/'+(requested_activity.learning_activity.uri).split('/')[1]+'.html',
                                  {'XML_NAV':XML,
                                   'uri':requested_activity.learning_activity.uri,
                                   'content':test,
                                   'feedback':feedback,
                                   'breadcrumbs':breadcrumbs,
                                   'uri_id':'/%s'% requested_activity.learning_activity.id,


                                   'attempt_limit':requested_activity.learning_activity.attempt_limit,
                                  'num_attempts': requested_activity.num_attempts,
                                   'attempts_left':attempts_left ,
                                   'root_id':'/%s'% requested_activity.learning_activity.get_root().id,

                                    'root':requested_activity.learning_activity.get_root().uri},

                                    context_instance=RequestContext(request))
    else:

        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.



def path_program(request,path_id, uri):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        try:
            requested_activity = UserLearningActivity.objects.get(learning_activity__id = path_id ,user = request.user )
        except ObjectDoesNotExist as e:
            return HttpResponseNotFound('<h1>Learning Activity not found</h1>')
        root = None
        try:
            root = UserLearningActivity.objects.get(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )
        except (ObjectDoesNotExist, IndexError) as e:
                return HttpResponseNotFound('<h1>Path not found</h1>')

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            # if choice_exit consider complete
            _set_current(request,requested_activity, root, s)

        # Gets the current navegation tree as XML
        _XML = get_nav(root)
        #Escape for javascript
        XML=ET.tostring(_XML,'utf-8').replace('"', r'\"')

        breadcrumbs = s.get_current_path(requested_activity)
        print Activity.get(requested_activity.learning_activity.uri),path_id,uri
        print requested_activity.learning_activity.uri
        return render_to_response('activitytree/program.html', {'program_quiz':Activity.get(requested_activity.learning_activity.uri),
                                                                'activity_uri':requested_activity.learning_activity.uri,
                                                                'uri_id':'%s'% requested_activity.learning_activity.id,

                                                                'breadcrumbs':breadcrumbs,
                                                                'root':requested_activity.learning_activity.get_root().uri,
                                                                'root_id':'/%s'% requested_activity.learning_activity.get_root().id,
                                                                'XML_NAV':XML
                                                                },
                                  context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)

@transaction.atomic
def program(request, uri):
    print request.path
    program_test = Activity.get(request.path)
    print 'ppt',program_test
    if program_test:
        return render_to_response('activitytree/program.html', {'program_quiz':program_test,
                                                        'activity_uri':request.path,
                                                        'breadcrumbs':None,
                                                        'root':None,
                                                        'XML_NAV':None
                                                        },
                          context_instance=RequestContext(request))
    else:

        return HttpResponseNotFound('<h1>Activity not found</h1>')

@csrf_protect
def execute_queue(request):
    if request.method == 'POST':
        rpc=json.loads(request.body)
        print rpc


        code = rpc["params"][0]
        activity_uri = rpc["method"]
        program_test = Activity.get(activity_uri)
        unit_test = program_test['unit_test']
        server = Cola(program_test['lang'])

        task = {"id": None, "method": "exec", "params": {"code": code, "test": unit_test}}
        task_id = server.enqueue(**task)

        if request.user.is_authenticated() and 'id' in rpc:
            ula = None
            try:
                ula = UserLearningActivity.objects.get(learning_activity__id=rpc["id"], user=request.user )

                s = SimpleSequencing()
                s.update(ula)
                ## Mouse Dynamics
                event = ULA_Event.objects.create(ULA=ula,context=rpc)
                event.save()
            except ObjectDoesNotExist:
                #Assume is a non assigned program
                print "Non"
                pass

        rpc['task_id']=task_id

        result= {"result":"added" , "error": None, "id": task_id}
        return HttpResponse(json.dumps(result), content_type='application/javascript')


@csrf_protect
def get_result(request):
    if request.method == 'POST':
        rpc=json.loads(request.body)
        #We only need the Task identifier
        #TO DO:
        # No ID, Task Not Found
        task_id = rpc["id"]
        t = Task(id=task_id)

        # outcome:
        # -1 No result found
        # 0 Sub-process Success
        # 1 Sub-process Failure
        if t.get_result(task_id.split(':')[0]):

            if t.result:
                string_json=""
                try:
                    string_json = json.loads( t.result[0])
                except Exception, e:
                    print e

                if request.user.is_authenticated():
                    try:
                        ula = UserLearningActivity.objects.get(learning_activity__uri=rpc["params"][0], user=request.user)
                        s = SimpleSequencing()

                        if string_json['result'] == 'Success':
                            s.update(ula, progress_status='completed', objective_status='satisfied', objective_measure=30,attempt=True)

                        else:
                            s.update(ula,attempt=True)
                    except Exception, e:
                        print e

                result = json.dumps({'result':string_json, 'outcome': t.result[1]})
                return HttpResponse(result , content_type='application/javascript')

            else:
                return HttpResponse(json.dumps({'outcome':-1}) , content_type='application/javascript')
        else:
            return HttpResponse(json.dumps({'outcome':-1}) , content_type='application/javascript')

def _get_learning_activity(uri):
    try:
        la = LearningActivity.objects.get(uri=uri)
    except ObjectDoesNotExist:
        return None
    return la




def _get_ula(request, uri):
    try:
        la = _get_learning_activity(uri)
        if la is None:
            return None
    except ObjectDoesNotExist:
        return None

    # Let's get the requested user learning activity
    try:
        requested_activity = UserLearningActivity.objects.filter(learning_activity__uri = uri ,user = request.user )[0]
    except (ObjectDoesNotExist, IndexError) as e:
        #User does not have a tracking activity tree
        #If the requested activity is the root of a tree
        #register the user to it
        return None
    return requested_activity

def _set_current(request,requested_activity, root, s,objective_status=None, progress_status=None):
    # Sets the requested  Learning Activity as current

    atree = ActivityTree.objects.get(user=request.user,root_activity=root.learning_activity.get_root())

    # Exits last activty
    if atree.current_activity:
        if request.method == 'GET' and atree.current_activity.learning_activity.choice_exit:
            objective_status='satisfied'
            progress_status='complete'
        s.exit( atree.current_activity, objective_status=objective_status, progress_status=progress_status)
    s.set_current(requested_activity)




def _check_quiz(post_dict, quiz):
    answerDict = dict(post_dict.iterlists())
    checked = {}
    for q in quiz['questions']:
        id = q['id']
        answer = q['answer']
        interaction = q['interaction']
        checked[id] = {}

        if interaction in ['choiceInteraction','simpleChoice']:
            if unicode(id) in answerDict:
                user = answerDict[unicode(id)]
                user_index = [ int(a.split("_")[-1]) for a in user]
                user_answer = [int(i in user_index) for i in range(len(answer))]

                if answer == user_answer:
                    checked[id]['correct'] = 1
                else:
                    checked[id]['correct'] = 0

                checked[id]['checked'] = [ (user_answer[i]==answer[i]) and (answer[i]==1) for i in range(len(answer))]
                checked[id]['user_answer']  = user_answer
            else:
                checked[id]['correct'] = 0
                checked[id]['checked'] = [False for _ in range(len(answer))]
                checked[id]['user_answer']  = [0 for _ in range(len(answer))]
        elif interaction in ['textEntryInteraction']:
            if unicode(id) in answerDict:
                user_answer = answerDict[unicode(id)][0]
                checked[id]['user_answer'] = user_answer

                if user_answer in answer :
                    checked[id]['correct'] = 1
                else:
                    checked[id]['correct'] = 0
    checked['total_correct'] = sum([float(checked[key]['correct']) for key in checked if key not in ['checked']])

    return checked

def _check_survey(post_dict, quiz):
    answerDict = dict(post_dict.iterlists())
    checked = {}
    for q in quiz['questions']:
        id = q['id']
        answer = q['answer']
        interaction = q['interaction']
        checked[id] = {}

        if interaction in ['choiceInteraction','simpleChoice']:
            if unicode(id) in answerDict:
                user = answerDict[unicode(id)]
                user_index = [ int(a.split("_")[-1]) for a in user]
                user_answer = [int(i in user_index) for i in range(len(answer))]

                if 1 in user_answer:
                    checked[id]['correct'] = 1
                else:
                    checked[id]['correct'] = 0

                checked[id]['checked'] = [ (user_answer[i]==answer[i]) and (answer[i]==1) for i in range(len(answer))]
                checked[id]['user_answer']  = user_answer
            else:
                checked[id]['correct'] = 0
                checked[id]['checked'] = [False for _ in range(len(answer))]
                checked[id]['user_answer']  = [0 for _ in range(len(answer))]
        elif interaction in ['textEntryInteraction']:
            if unicode(id) in answerDict:
                user_answer = answerDict[unicode(id)][0]
                checked[id]['user_answer'] = user_answer

                if True :
                    checked[id]['correct'] = 1
                else:
                    checked[id]['correct'] = 0
    checked['total_correct'] = sum([float(checked[key]['correct']) for key in checked if key not in ['checked']])

    return checked

def login_view(request,template_name='registration/login.html',  redirect_field_name=REDIRECT_FIELD_NAME):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {}

        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.GET:
                    request.session['after_login'] = request.GET['next']
                    return HttpResponseRedirect(request.GET['next'])
                else:

                    return HttpResponseRedirect('/')


                # Redirect to a success page.
            else:

                context['errors'] = 'User is locked'

        else:
            context['errors'] = 'Invalid Login'

        return TemplateResponse(request, template_name,context, current_app=None)

    else:
            return TemplateResponse(request, template_name, current_app=None)



def ajax_vote(request, type, uri):
    activity_uri = request.path[len('/ajax_vote'):]
    if request.user.is_authenticated():
        if request.method == 'POST':
            activity = UserLearningActivity.objects.filter(learning_activity__uri = activity_uri ,user = request.user )[0]
            activity.user_rating = int(request.POST['rate'])
            activity.save()

        vals = UserLearningActivity.objects.filter(learning_activity__uri = activity_uri).aggregate(Avg('user_rating'),Count('user_rating'))
        response_data = {'avg': vals['user_rating__avg'], 'votes': vals['user_rating__count']}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(content="Ya voto?")



def facebook_get_login(request):
    state = request.session.session_key
    url = """https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&state=%s""" % \
              (settings.FACEBOOK_APP_ID ,settings.FACEBOOK_REDIRECT_URL,
               state
                )

    return HttpResponseRedirect(url)

def facebook_login(request):
    if 'error' in request.GET:
        return HttpResponseRedirect('/')


    code = request.GET['code']
    UID = request.GET['state']


    args = { "client_id" : settings.FACEBOOK_APP_ID,
             "redirect_uri" : settings.FACEBOOK_REDIRECT_URL ,
             "client_secret" : settings.FACEBOOK_APP_SECRET,
             "code" : code }


    response = urllib.urlopen( "https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(args))

    response = urlparse.parse_qs(response.read())
    access_token = response["access_token"][-1]
    profile = json.load(urllib.urlopen(
        "https://graph.facebook.com/me?" +
        urllib.urlencode(dict(access_token=access_token))))
    expires = response['expires'][0]

    facebook_session = FacebookSession.objects.get_or_create(
        access_token=access_token)[0]

    facebook_session.expires = expires
    facebook_session.save()


    user = authenticate(token=access_token)
    if user:
        if user.is_active:
            login(request, user)
            if 'after_login' in request.session:
                return HttpResponseRedirect(request.session['after_login'])
            return HttpResponseRedirect('/')
        else:
            error = 'AUTH_DISABLED'

    if 'error_reason' in request.GET:
        error = 'AUTH_DENIED'
    ### TO DO Log Error
    return HttpResponseRedirect('/')

@csrf_protect
def rate_object(request):
    if request.method == 'POST':
        vote=json.loads(request.body)
        la = LearningActivity.objects.get(uri=vote["uri"] )


        rating = LearningActivityRating(user=request.user,learning_activity=la,rating= vote["rating"], context=0)
        rating.save()

        result= {"result":"added" , "error": None, "id": None}
        return HttpResponse(json.dumps(result), content_type='application/javascript')




@login_required
def logout_view(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')


def update_pool(uri):
    if uri:
        if uri in multi_device_activities:
            for device in multi_device_activities[uri]:
                print device
                redis_service.set(device["dispositivo"],{"url":ip_couch + device["url"] ,"estado":device["estado"],"tipo":device["tipo"]} )

