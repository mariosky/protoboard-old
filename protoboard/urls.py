from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
      (r'^$','activitytree.views.welcome'),
      (r'^welcome/$','activitytree.views.welcome'),
     (r'^activity/(?P<uri>\w+)$','activitytree.views.activity'),
      (r'^test/(?P<uri>\w+)$','activitytree.views.test'),

      (r'^program/(?P<uri>\w+)$','activitytree.views.program'),
      (r'^execute_queue$','activitytree.views.execute_queue'),
      (r'^get_result$','activitytree.views.get_result'),

      (r'^ajax_vote/(?P<type>\w+)/(?P<uri>\w+)$','activitytree.views.ajax_vote'),
      (r'^login/$', 'activitytree.views.login', {'template_name': 'registration/login.html'}),
      url(r'^logout/$', 'activitytree.views.logout'),
      # Hack horrible para el logout
      (r'^accounts/login/$', 'activitytree.views.welcome'),
      url('', include('social.apps.django_app.urls', namespace='social')),



    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
