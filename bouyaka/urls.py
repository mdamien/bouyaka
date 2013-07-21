from django.conf.urls import patterns, include, url

from canary import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index),
    url(r'^r/(?P<line>\S+)', views.r13),
    url(r'^(?P<line>\S+)', views.tell),
)
