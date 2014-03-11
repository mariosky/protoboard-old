# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.utils import simplejson
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from activitytree.models import Course,ActivityTree,UserLearningActivity, LearningActivity,LearningStyleInventory
from activitytree.interaction_handler import SimpleSequencing
from activitytree.activities import activities

from eval_code.RedisCola import Cola, Task
import json


def welcome(request):
    courses = Course.objects.all()

    return render_to_response('activitytree/welcome.html', {'courses':courses}, context_instance=RequestContext(request))

def activity(request, uri, objective_status = None):

    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request, s)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            _set_current(request,requested_activity, root, s, objective_status='satisfied', progress_status='complete')

        if request.method == 'POST' and 'nav_event' in request.POST:
        # We are going to exit activity, get objective measure
            objective_measure = float(request.POST['objective_measure'])



            next_uri = None
            if  request.POST['nav_event'] == 'next':
                # Go TO NEXT ACTIVITY
                next_uri = s.get_next(root)
                print next_uri

            elif request.POST['nav_event'] == 'prev':
                # Go TO PREV ACTIVITY
                next_uri = s.get_prev(root)
            print next_uri

            if next_uri is None:
                    #No more activities ?
                return HttpResponseRedirect( root.learning_activity.uri)

            else:
                s.exit( requested_activity, progress_status = 'complete', objective_status = 'satisfied', objective_measure = objective_measure)
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)


        # Gets the current navegation tree as HTML
        nav = s.get_nav(root)
        navegation_tree = s.nav_to_html(nav)

        ####
        ####
        ####


        content = activities[requested_activity.learning_activity.uri]

        return render_to_response('activitytree/'+ (requested_activity.learning_activity.uri).split('/')[1]+'.html',

                                  {'navegation': navegation_tree,
                                   'uri':requested_activity.learning_activity.uri,
                                   'content':content},
                                    context_instance=RequestContext(request))

        #####
        #####
        #####



    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.    


def test(request, uri, objective_status = None):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request, s)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]
        feedback = None

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            _set_current(request,requested_activity, root, s, objective_status='satisfied', progress_status='complete')


        elif request.method == 'POST':
            if 'check' in request.POST:
                feedback = _check_quiz(request.POST, activities[requested_activity.learning_activity.uri])
                # Exits the current Learning Activity
                objective_measure = feedback['total_correct']
                s.update(requested_activity, progress_status = None, objective_status = None, objective_measure = objective_measure)

            elif 'nav_event' in request.POST:
                next_uri = None

                if request.POST['nav_event'] == 'next' :
                    # Go TO NEXT ACTIVITY
                    next_uri = s.get_next(root)
                elif request.POST['nav_event'] == 'prev':
                    # Go TO PREV ACTIVITY
                    next_uri = s.get_prev(root)

                if next_uri is None:
                        #No more activities ?
                    return HttpResponseRedirect( root.learning_activity.uri)
                else:
                    next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                    return HttpResponseRedirect(next_activity.learning_activity.uri)

       # Gets the current navegation tree as HTML

        nav = s.get_nav(root)
        navegation_tree = s.nav_to_html(nav)

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
                                   'feedback':feedback},
                                    context_instance=RequestContext(request))
    else:      
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.




def program(request,uri):
    if request.user.is_authenticated():
        s = SimpleSequencing()
        # First, the requested_activity  exists??
        # Gets the Learning Activity object from uri
        requested_activity = _get_ula(request, s)

        if not requested_activity:
            return HttpResponseNotFound('<h1>Activity not found</h1>')

        # Gets the root of the User Learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = requested_activity.learning_activity.get_root() ,user = request.user )[0]

        if request.method == 'GET':
            # Exits last activity, and sets requested activity as current
            _set_current(request,requested_activity, root, s, objective_status='satisfied', progress_status='complete')

        if request.method == 'POST' and 'nav_event' in request.POST:
        # We are going to exit activity, get objective measure
            objective_measure = float(request.POST['objective_measure'])



            next_uri = None
            if  request.POST['nav_event'] == 'next':
                # Go TO NEXT ACTIVITY
                next_uri = s.get_next(root)
                print next_uri

            elif request.POST['nav_event'] == 'prev':
                # Go TO PREV ACTIVITY
                next_uri = s.get_prev(root)
            print next_uri

            if next_uri is None:
                    #No more activities ?
                return HttpResponseRedirect( root.learning_activity.uri)

            else:
                s.exit( requested_activity, progress_status = 'complete', objective_status = 'satisfied', objective_measure = objective_measure)
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)


        # Gets the current navegation tree as HTML
        nav = s.get_nav(root)
        navegation_tree = s.nav_to_html(nav)



        return render_to_response('activitytree/program.html', {'program_quiz':activities[request.path],
                                                                'activity_uri':request.path,
                                                                'navegation': navegation_tree
                                                                },
                                  context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.


def execute_queue(request):
    if request.method == 'POST':
        rpc=json.loads(request.body)

        server = Cola("curso")

        code = rpc["params"][0]
        activity_uri = rpc["method"]
        unit_test = activities[activity_uri]['unit_test']

        task = {"id": None,"method": "exec","params": {"code": code, "test":unit_test }}
        task_id = server.enqueue(**task)

        print 'TASK:',task_id, task

        result= {"result":"added" , "error": None, "id": task_id}
        return HttpResponse(json.dumps(result), mimetype='application/javascript')

def get_result(request):
    if request.method == 'POST':
        rpc=json.loads(request.body)
        #We only need the Task identifier
        #TO DO:
        # No ID, Task Not Found
        task_id = rpc["id"]
        print task_id
        t = Task(id=task_id)
        print t

        # outcome:
        # -1 No result found
        # 0 Sub-process Success
        # 1 Sub-process Failure
        if t.get_result('curso'):
            result = json.dumps({'result': t.result[0], 'outcome': t.result[1]})
            return HttpResponse(result , mimetype='application/javascript')

        else:
            return HttpResponse(json.dumps({'outcome':-1}) , mimetype='application/javascript')


def _get_ula(request, s):
    try:
        la = LearningActivity.objects.filter(uri=request.path)[0]
    except ObjectDoesNotExist:
        return None

    # Let's get the requested user learning activity
    try:
        requested_activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user )[0]
    except ObjectDoesNotExist:
        #User does not have a tracking activity tree
        #If the requested activity is the root of a tree
        #register the user to it
        if la and la.root is None:
            s.assignActivityTree(request.user,la)
            requested_activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user)[0]
        #If is not a root learning activity then sorry, not found
        else:
            return None
    return requested_activity

def _set_current(request,requested_activity, root, s,objective_status, progress_status):
    # Sets the requested  Learning Activity as current
    atree = ActivityTree.objects.get(user=request.user,root_activity=root.learning_activity.get_root())
    # Exits last activty
    if atree.current_activity:
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
                print user_answer, answer

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




def ajax_vote(request, type, uri):
    activity_uri = request.path[len('/ajax_vote'):]
    if request.user.is_authenticated():
        if request.method == 'POST':
            activity = UserLearningActivity.objects.filter(learning_activity__uri = activity_uri ,user = request.user )[0]
            activity.user_rating = int(request.POST['rate'])
            activity.save()

        vals = UserLearningActivity.objects.filter(learning_activity__uri = activity_uri).aggregate(Avg('user_rating'),Count('user_rating'))
        response_data = {'avg': vals['user_rating__avg'], 'votes': vals['user_rating__count']}

        return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
    else:
        return HttpResponse(content="Ya voto?")
