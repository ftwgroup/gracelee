from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/$', 'photo_gallery.views.image_info'),
    url(r'^(?P<height>[\d]+)[Xx](?P<width>[\d]+)/(?P<url>[\w\-\.:/]+)/$',
    	'photo_gallery.views.image_resize'),
    url(r'^(?P<left>[\d]+)[Xx](?P<top>[\d]+)-(?P<right>[\d]+)[Xx](?P<bottom>[\d]+)/(?P<url>[\w/-_.]+)/$',
    	'photo_gallery.views.image_crop'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                })
    )