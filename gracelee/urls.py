from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', TemplateView.as_view(template_name="index.html")),
    url(r'^graceInternal/$', TemplateView.as_view(template_name="graceInternal.html")),
    url(r'^graceContact_form/$', TemplateView.as_view(template_name="graceContact_form.html")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                })
    )