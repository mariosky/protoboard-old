from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
      (r'^index.html$','activitytree.views.index'),
      (r'^activity/(?P<uri>\w+)$','activitytree.views.activity'),
      (r'^bye/(?P<uri>\w+)$','activitytree.views.bye'),
      (r'^test/(?P<uri>\w+)$','activitytree.views.test'),
      (r'^ajax_vote/(?P<type>\w+)/(?P<uri>\w+)$','activitytree.views.ajax_vote'),
      (r'^protoboard/index.html$','activitytree.views.index'),
      (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
      (r'^logout/$', 'django.contrib.auth.views.logout_then_login')
      
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
