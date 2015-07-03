from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()





urlpatterns = patterns('',
    # Example:
      (r'^$','activitytree.views.welcome'),
      (r'^welcome/$','activitytree.views.welcome'),
      (r'^dashboard/(?P<path_id>[0-9]+)$','activitytree.views.dashboard'),

      (r'^(?P<uri>activity/([\w+](\/*)(-*))+)$','activitytree.views.activity'),
      (r'^(?P<path_id>[0-9]+)(?P<uri>/activity/([\w+](\/*)(-*))+)$','activitytree.views.path_activity'),

      (r'^(?P<path_id>[0-9]+)(?P<uri>/test/([\w+](\/*)(-*))+)$','activitytree.views.path_test'),

      (r'^(?P<path_id>[0-9]+)(?P<uri>/program/([\w+](\/*)(-*))+)$','activitytree.views.path_program'),

      (r'^(?P<uri>program/([\w+](\/*)(-*))+)$','activitytree.views.program'),

      (r'^execute_queue$','activitytree.views.execute_queue'),
      (r'^javascript_result$','activitytree.views.javascript_result'),
      (r'^get_activities$','activitytree.views.get_activities'),

      (r'^get_result$','activitytree.views.get_result'),

      (r'^rate_object$','activitytree.views.rate_object'),
      (r'^facebook/get_login/?$', 'activitytree.views.facebook_get_login'),
      (r'^facebook/login/?$','activitytree.views.facebook_login'),
      (r'^logout/?$', 'activitytree.views.logout_view'),
      (r'^login/$', 'activitytree.views.login_view', {'template_name': 'registration/login.html'}),

      url(r'^logout/$', 'activitytree.views.logout'),
      # Hack horrible para el logout
      (r'^accounts/login/$', 'activitytree.views.welcome'),
      url('', include('django.contrib.auth.urls')),
      #url('', include('social.apps.django_app.urls', namespace='social')),



    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
