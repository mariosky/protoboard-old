# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.db.models import Avg, Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.sites.models import get_current_site
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.template import RequestContext
from django.db import transaction



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View


from activitytree.models import Course,ActivityTree,UserLearningActivity, LearningActivity, ULA_Event, FacebookSession,LearningActivityRating
from activitytree.interaction_handler import SimpleSequencing
from activitytree.activities import activities

#from social.backends.google import GooglePlusAuth

import urllib
import urlparse

from eval_code.RedisCola import Cola, Task
import json
from django.conf import settings

# def logout(request):
#     """Logs out user"""
#     auth_logout(request)
#     plus_scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
#     plus_id=settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY
#     courses = Course.objects.all()
#     return render_to_response('activitytree/welcome.html', {'courses':courses,'plus_scope':plus_scope,'plus_id':plus_id}
#                              , RequestContext(request))

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


def activity(request,uri):
    learning_activity = _get_learning_activity(request)
    root=None
    if learning_activity is None:
        return HttpResponseNotFound('<h1>Learning Activity not found</h1>')


    if request.user.is_authenticated():
        s = SimpleSequencing()
        requested_activity = None
        if request.method == 'GET':
            requested_activity = _get_ula(request)

            # The requested_activity was NOT FOUND
            if not requested_activity : # The requested_activity was not found
            # Maybe a
            # 'start' REQUEST?
                if 'nav' in request.GET and request.GET['nav'] == 'start':
                    if learning_activity and learning_activity.root is None:
                        s.assignActivityTree(request.user,learning_activity)
                        requested_activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user)[0]
                        _set_current(request,requested_activity, requested_activity, s)
                    #If is not a root learning activity then sorry, not found
                    else:
                        return HttpResponseNotFound('<h1>Activity not found</h1>')
            #Else NOT FOUND
                return HttpResponseNotFound('<h1>Activity not found</h1>')

            # We have a valid requested_activity, lets handle OTHER NAVIGATION REQUEST

            #Get root of activity tree
            root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root(),
                                                       user = request.user )[0]
            # 'continue' REQUEST?
            if requested_activity.is_root() and 'nav' in request.GET and request.GET['nav'] == 'continue':
                current_activity = s.get_current(requested_activity)
                if current_activity:
                    requested_activity = current_activity
                    return HttpResponseRedirect( requested_activity.learning_activity.uri)
                else:
                    _set_current(request,requested_activity, root, s, objective_status=None, progress_status=None)
            #Else is a
            # 'choice' REQUEST
            else:
                _set_current(request,requested_activity, root, s)

        if request.method == 'POST' and 'nav_event' in request.POST:
            #Get root of activity tree
            root = _get_ula(request)
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

            #No more activities ?
            if next_uri is None:

                return HttpResponseRedirect( root.learning_activity.uri)
            else:
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)


        # Gets the current navegation tree as HTML
        nav = s.get_nav(root)
        XML_ = s.nav_to_xml(root=nav)
        #Escape for javascript
        XML=XML_.replace('"', r'\"')
        navegation_tree = s.nav_to_html(nav)

        breadcrumbs = s.get_current_path(requested_activity)


        ####
        ####
        ####


        content = activities[requested_activity.learning_activity.uri]

        if (requested_activity.learning_activity.uri).split('/')[2] =='video':
            print "VIDEO",(requested_activity.learning_activity.uri).split('/')[2]
            return render_to_response('activitytree/video.html',

                                  {'navegation': navegation_tree,
                                   'uri':requested_activity.learning_activity.uri,
                                   'video':content,
                                   'breadcrumbs':breadcrumbs,
                                   'root':requested_activity.learning_activity.get_root().uri},
                                    context_instance=RequestContext(request))

        elif requested_activity.learning_activity.is_container:

            return render_to_response('activitytree/container.html',

                                  {'navegation': navegation_tree,
                                   'XML_NAV':XML,
                                   'children': requested_activity.get_children(),
                                   'uri':requested_activity.learning_activity.uri,
                                   'content':content,
                                   'root':requested_activity.learning_activity.get_root().uri,
                                   'breadcrumbs':breadcrumbs},
                                    context_instance=RequestContext(request))
        else:
            return render_to_response('activitytree/'+ (requested_activity.learning_activity.uri).split('/')[1]+'.html',

                                  {'navegation': navegation_tree,
                                   'uri':requested_activity.learning_activity.uri,
                                   'root':requested_activity.learning_activity.get_root().uri,
                                   'content':content,
                                   'breadcrumbs':breadcrumbs},
                                    context_instance=RequestContext(request))

        #####
        #####
        #####

    else:
        try:
            la = LearningActivity.objects.filter(uri=request.path)[0]
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Check if public, all public for now
        if False:
            return HttpResponseRedirect('/login/?next=%s' % request.path)

        content = activities[la.uri]
        if (la.uri).split('/')[2] =='video':
            print "VIDEO",(la.uri).split('/')[2]
            return render_to_response('activitytree/video.html',

                                  {'navegation': None,
                                   'uri':la.uri,
                                   'video':content,
                                   'breadcrumbs':None },
                                    context_instance=RequestContext(request))

        elif la.is_container:
            return HttpResponseRedirect('/login/?next=%s' % request.path)


        else:
            return render_to_response('activitytree/'+ (la.uri).split('/')[1]+'.html',

                                  {'navegation': None,
                                   'uri':la.uri,
                                   'content':content,
                                   'breadcrumbs':None,
                                   },
                                    context_instance=RequestContext(request))


        # Do something for anonymous users.    

@transaction.atomic
def test(request, uri, objective_status = None):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]
        feedback = None

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            # if choice_exit consider complete
            _set_current(request,requested_activity, root, s, objective_status=None, progress_status=None)

        elif request.method == 'POST':
            if 'check' in request.POST:

                feedback = _check_quiz(request.POST, activities[requested_activity.learning_activity.uri])
                print feedback
                # Updates the current Learning Activity
                objective_measure = feedback['total_correct']
                if objective_measure >= activities[requested_activity.learning_activity.uri]['satisfied_at_least']:
                    objective_status='satisfied'
                else:
                    objective_status='notSatisfied'

                s.update(requested_activity, progress_status = None, objective_status = objective_status, objective_measure = objective_measure)

       # Gets the current navegation tree as HTML

        nav = s.get_nav(root)
        navegation_tree = s.nav_to_html(nav)
        breadcrumbs = s.get_current_path(requested_activity)



        content = activities[requested_activity.learning_activity.uri]
        if feedback:
            for q in content['questions']:
                if q['id'] in feedback:
                    q['feedback'] = feedback[q['id']]
                    if q['interaction']  in ['choiceInteraction','simpleChoice']:
                        q['feedback_options'] = zip(q['options'], feedback[q['id']]['user_answer'], feedback[q['id']]['checked'])

        return render_to_response('activitytree/'+(requested_activity.learning_activity.uri).split('/')[1]+'.html',
                                  {'navegation': navegation_tree,
                                   'uri':requested_activity.learning_activity.uri,
                                   'content':content,
                                   'feedback':feedback,
                                   'breadcrumbs':breadcrumbs,
                                    'root':requested_activity.learning_activity.get_root().uri},
                                    context_instance=RequestContext(request))
    else:

        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.

@transaction.atomic
def survey(request, uri, objective_status = None):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]
        feedback = None

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            # if choice_exit consider complete
            _set_current(request,requested_activity, root, s, objective_status=None, progress_status=None)

        elif request.method == 'POST':
            if 'check' in request.POST:

                feedback = _check_survey(request.POST, activities[requested_activity.learning_activity.uri])

                event = ULA_Event.objects.create(ULA=requested_activity,context=feedback)
                event.save()


                # Updates the current Learning Activity
                objective_measure = feedback['total_correct']
                #if objective_measure >= activities[requested_activity.learning_activity.uri]['satisfied_at_least']:
                objective_status='satisfied'
                #else:
                #    objective_status='notSatisfied'

                s.update(requested_activity, progress_status = None, objective_status = objective_status, objective_measure = objective_measure)

      # Gets the current navegation tree as HTML

        nav = s.get_nav(root)

        navegation_tree = s.nav_to_html(nav)

        breadcrumbs = s.get_current_path(requested_activity)

        content = activities[requested_activity.learning_activity.uri]


        if feedback:
            for q in content['questions']:
                if q['id'] in feedback:
                    q['feedback'] = feedback[q['id']]
                    if q['interaction']  in ['choiceInteraction','simpleChoice']:
                        q['feedback_options'] = zip(q['options'], feedback[q['id']]['user_answer'], feedback[q['id']]['checked'])

        return render_to_response('activitytree/'+(requested_activity.learning_activity.uri).split('/')[1]+'.html',
                                  {'navegation': navegation_tree,
                                   'uri':requested_activity.learning_activity.uri,
                                   'content':content,
                                   'feedback':feedback,
                                   'breadcrumbs':breadcrumbs,
                                   'root':requested_activity.learning_activity.get_root().uri},
                                    context_instance=RequestContext(request))
    else:      
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.


@transaction.atomic
def program(request,uri):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            # if choice_exit consider complete
            _set_current(request,requested_activity, root, s)

        # Gets the current navegation tree as HTML
        nav = s.get_nav(root)
        navegation_tree = s.nav_to_html(nav)
        breadcrumbs = s.get_current_path(requested_activity)

        return render_to_response('activitytree/program.html', {'program_quiz':activities[requested_activity.learning_activity.uri],
                                                                'activity_uri':requested_activity.learning_activity.uri,
                                                                'navegation': navegation_tree,
                                                                'breadcrumbs':breadcrumbs,
                                                                'root':requested_activity.learning_activity.get_root().uri
                                                                },
                                  context_instance=RequestContext(request))

    else:
        try:
            la = LearningActivity.objects.filter(uri=request.path)[0]
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Activity not found</h1>')
            # Check if public, all public for now
        if False:
            return HttpResponseRedirect('/login/?next=%s' % request.path)

        content = activities[la.uri]
        if request.method == 'GET':
            return render_to_response('activitytree/program.html', {'program_quiz':activities[la.uri],
                                                                'activity_uri':la.uri,
                                                                'navegation': None,
                                   'breadcrumbs':None
                                                                },
                                  context_instance=RequestContext(request))



        #return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.

@csrf_protect
def execute_queue(request):
    if request.method == 'POST':
        rpc=json.loads(request.body)
        server = Cola("curso")

        code = rpc["params"][0]
        activity_uri = rpc["method"]
        unit_test = activities[activity_uri]['unit_test']

        task = {"id": None, "method": "exec", "params": {"code": code, "test": unit_test}}
        task_id = server.enqueue(**task)

        if request.user.is_authenticated():
            ula = UserLearningActivity.objects.get(learning_activity__uri=rpc["method"], user=request.user )
            s = SimpleSequencing()
            s.update(ula)
            ## Mouse Dynamics
            event = ULA_Event.objects.create(ULA=ula,context=rpc)
            event.save()

        rpc['task_id']=task_id

        result= {"result":"added" , "error": None, "id": task_id}
        return HttpResponse(json.dumps(result), mimetype='application/javascript')


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
        if t.get_result('curso'):

            if t.result:

                string_json = json.loads( t.result[0])
                if string_json['result'] == 'Success':
                    if request.user.is_authenticated():
                        ula = UserLearningActivity.objects.get(learning_activity__uri=rpc["params"][0], user=request.user)

                        s = SimpleSequencing()
                        s.update(ula, progress_status='completed', objective_status='satisfied', objective_measure=100)
                result = json.dumps({'result':string_json, 'outcome': t.result[1]})
                return HttpResponse(result , mimetype='application/javascript')

            else:
                return HttpResponse(json.dumps({'outcome':-1}) , mimetype='application/javascript')
        else:
            return HttpResponse(json.dumps({'outcome':-1}) , mimetype='application/javascript')

def _get_learning_activity(request):
    try:
        la = LearningActivity.objects.filter(uri=request.path)[0]
    except ObjectDoesNotExist:
        return None
    return la


def _get_ula(request):
    try:
        la = _get_learning_activity(request)
        if la is None:
            return None
    except ObjectDoesNotExist:
        return None

    # Let's get the requested user learning activity
    try:
        requested_activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user )[0]
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

        return HttpResponse(json.dumps(response_data), mimetype="application/json")
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

    print code, args

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
    print "Usuario",user
    if user:
        if user.is_active:
            login(request, user)
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
        return HttpResponse(json.dumps(result), mimetype='application/javascript')




@login_required
def logout_view(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')