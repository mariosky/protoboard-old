# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.utils import simplejson
from django.db.models import Avg, Count

from activitytree.models import LearningActivity, UserProfile, LearningStyleInventory,ActivityTree,UserLearningActivity
from activitytree.interaction_handler import SimpleSequencing
from activitytree.activities import activities




def index(request):
    if request.user.is_authenticated():
        # Bring the root ULA (default lesson) , in this case Unit
        # We can have different lessons this can be done with adding  root parameter
        root = UserLearningActivity.objects.filter(learning_activity__uri = "/activity/POO" ,user = request.user )[0]
        s = SimpleSequencing()
        atree = ActivityTree.objects.get(user=root.user,root_activity=root.learning_activity)

        #if the student has a current activity return it
        if atree.current_activity:
            activity =  atree.current_activity
            return HttpResponseRedirect(activity.learning_activity.uri)
        #else get the next activity to start the lesson
        else:
            # Go TO NEXT ACTIVITY
            next_uri = s.get_next(root)
            if next_uri is None:
                #Go to Root
                return HttpResponseRedirect(root.learning_activity.uri)
            else:
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    # Do something for anonymous users.
    

def activity(request, uri, objective_status = None):
    if request.user.is_authenticated():
        # Gets the Learning Activity object from id
        activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user )[0]

        s = SimpleSequencing()
        # Exits the current LA if there is one, but with out setting an objective_measure
        # Must EXIT ??
        # Gets the root of the learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = activity.learning_activity.get_root() ,user = request.user )[0]
        # activity.get_root()
        nav = s.get_nav(root)

        if request.method == 'GET':
            # Sets the Learning Activity as current
            atree = ActivityTree.objects.get(user=activity.user,root_activity=root.learning_activity.get_root())
            if atree.current_activity:
                s.exit( atree.current_activity, objective_status = 'satisfied', progress_status = 'complete' )
            s.set_current(activity)
        elif request.method == 'POST':
            # Get NEXT ACTIVITY
            next_uri = s.get_next(root)
            print request.POST
            # Exits the current Learning Activity
            objective_measure = float(request.POST['objective_measure'])
            s.exit( activity, progress_status = 'complete', objective_status = 'satisfied', objective_measure = objective_measure)

            if next_uri is None:
                #No more activities ?
                return HttpResponseRedirect('/bye'+ root.learning_activity.uri[len("/activity"):] )

            else:
                #### Change id to URI
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)
       
        # Gets the current navegation tree as HTML
        navegation_tree = s.nav_to_html(nav)
        ls = request.user.learningstyleinventory
        content = activities[activity.learning_activity.uri]
        lsi_graphic =  "http://chart.apis.google.com/chart?cht=r&chs=200x200&chd=t:" + str(ls.visual*100/25)+","+ str(ls.verbal*100/25)+","+str(ls.aural*100/25)+","+str(ls.physical*100/25)+","+str(ls.logical*100/25)+","+str(ls.social*100/25)+","+str(ls.solitary*100/25)+ "&chco=FF0000&chls=2.0,4.0,0.0&chxt=x&chxl=0:|visual|verbal|aural|fisico|logico|social|solitario&chxr=0,0.0,25.0&chm=B,FF000080,0,1.0,5.0"
        return render_to_response('activitytree/' + (activity.learning_activity.uri).split('/')[1]+'.html', {'navegation': navegation_tree, 'uri':activity.learning_activity.uri,'lsi_graphic':lsi_graphic,'content':content},context_instance=RequestContext(request))
    else:      
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.    


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

def test(request, uri, objective_status = None):
    if request.user.is_authenticated():
        # Gets the Learning Activity object from id
        
        activity = UserLearningActivity.objects.filter(learning_activity__uri = request.path ,user = request.user )[0]
       
        s = SimpleSequencing()
        # Exits the current LA if there is one, but with out setting an objective_mesure
        # Gets the root of the learning Activity
        root = UserLearningActivity.objects.filter(learning_activity = activity.learning_activity.root ,user = request.user )[0]

        if request.method == 'GET':
            # Sets the Learning Activity as current
            atree = ActivityTree.objects.get(user=activity.user,root_activity=activity.learning_activity.root)
            if atree.current_activity:
                s.exit( atree.current_activity, objective_status = 'satisfied', progress_status = 'complete' )
            
            s.set_current(activity)
            
        elif request.method == 'POST':
            # Exits the current Learning Activity
            objective_measure = sum([int(request.POST[key]) for key in request.POST if key[:8] == 'question' ])
            s.exit(activity, progress_status = None, objective_status = 'satisfied', objective_measure = objective_measure)
            # Exits the current LA if there is one, but with out setting an objective_mesure
            # Go TO NEXT ACTIVITY
            next_uri = s.get_next(root)
            if next_uri is None:
                #No more activities ?
                pass
            else:
                next_activity = UserLearningActivity.objects.filter(learning_activity__uri = next_uri ,user = request.user )[0]
                return HttpResponseRedirect(next_activity.learning_activity.uri)


        nav = s.get_nav(root)
        # Gets the current navegation tree as HTML
        navegation_tree = s.nav_to_html(nav)
        ls = request.user.learningstyleinventory
        content = activities[activity.learning_activity.uri]
        lsi_graphic =  "http://chart.apis.google.com/chart?cht=r&chs=200x200&chd=t:" + str(ls.visual*100/25)+","+ str(ls.verbal*100/25)+","+str(ls.aural*100/25)+","+str(ls.physical*100/25)+","+str(ls.logical*100/25)+","+str(ls.social*100/25)+","+str(ls.solitary*100/25)+ "&chco=FF0000&chls=2.0,4.0,0.0&chxt=x&chxl=0:|visual|verbal|aural|fisico|logico|social|solitario&chxr=0,0.0,25.0&chm=B,FF000080,0,1.0,5.0"
        return render_to_response('activitytree/'+(activity.learning_activity.uri).split('/')[1]+'.html', {'navegation': navegation_tree, 'uri':activity.learning_activity.uri,  'lsi_graphic':lsi_graphic,'content':content},context_instance=RequestContext(request))
    else:      
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.

def bye(request, uri ):
    if request.user.is_authenticated():
        # Gets the Learning Activity object from id

        root = UserLearningActivity.objects.filter(learning_activity__uri = "/activity/"+ uri  ,user = request.user )[0]
        s = SimpleSequencing()
        nav = s.get_nav(root)

        if request.method == 'GET':
            # Sets the Learning Activity as current
            navigation_tree = s.nav_to_html(nav)
            ls = request.user.learningstyleinventory
            content = activities[request.path]
            lsi_graphic =  "http://chart.apis.google.com/chart?cht=r&chs=200x200&chd=t:" + str(ls.visual*100/25)+","+ str(ls.verbal*100/25)+","+str(ls.aural*100/25)+","+str(ls.physical*100/25)+","+str(ls.logical*100/25)+","+str(ls.social*100/25)+","+str(ls.solitary*100/25)+ "&chco=FF0000&chls=2.0,4.0,0.0&chxt=x&chxl=0:|visual|verbal|aural|fisico|logico|social|solitario&chxr=0,0.0,25.0&chm=B,FF000080,0,1.0,5.0"
            return render_to_response('activitytree/bye.html', {'uri':'/bye/' + uri,'content':content},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
        # Do something for anonymous users.
    
