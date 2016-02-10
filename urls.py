# -*- coding: utf-8 -*- 

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
SR = settings.STATIC_ROOT

urlpatterns = patterns('',)

urlpatterns += patterns('',
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('main.views',
    (r'^tag-list.js$', 'tagListJS'),
    (r'^autocomplete-list.js$', 'autocompleteListJS'),
    (r'^ajax/logo/$', 'ajaxLogo'),
    (r'^ajax/logo/([\d,]+)/$', 'ajaxLogoByIdList'),
    (r'^dragtest/$', 'dragtest'),
    
    (r'^$', 'index'),
    (r'^blog/([\-\d\w]+)/$', 'blog'),
    (r'^blog/([\-\d\w]+)/page-(/d+)/$', 'blog'),
    (r'^post/(\d+)/$', 'post'),
    # (r'^post/(\d+)/edit/', 'postEdit'),
    # (r'^post/(\d+)/delete/', 'postDelete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', 'main.views._404'),
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': SR+'/img/'}),
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': SR+'/js/'}),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': SR+'/css/'}),
    )

urlpatterns += patterns('main.views',
    (r'^([\-\d\w]+)/$', 'page'),
)

