from django.conf.urls import patterns, include, url

from canary import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<name>\S+)/(?P<line>\S+)', views.tell),
    url(r'^/tell/(?P<name>\S+)/(?P<line>\S+)', views.tell),
    url(r'^/dit/(?P<name>\S+)/(?P<line>\S+)', views.tell),
)
