from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^(\+\+.*\+\+/)?geo', 'ngt.geo.views.rpc_handler'),
                       (r'^assets/?$', 'ngt.assets.views.list'),
                       (r'^assets/(\d+)$', 'ngt.assets.views.'),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
                       (r'^admin/(.*)', admin.site.root),
                       
                       #Job Management
                       (r'^dispatch/?$', 'dispatch.views.index'),
                       (r'^dispatch/job/?$', 'dispatch.views.jobber'),
                       
                       #The Big Board!
                       (r'bigboard/?$', 'ngt.bigboard.views.index'),
                       (r'bigboard/reapers/?$', 'ngt.bigboard.views.list_reapers'),
                       (r'bigboard/jobs/?$', 'ngt.bigboard.views.list_jobsets'),
                       (r'bigboard/jobs/(?P<jobset_id>\d+)$', 'ngt.bigboard.views.jobset_detail'),
                       (r'bigboard/jobs/new/?$', 'ngt.bigboard.views.jobset_create'),
           
                       #(r'^(.*)$', 'ngt.views.index'),
                       (r'^/?$', 'ngt.views.index'),
                      
)
