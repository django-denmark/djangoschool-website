from django.conf.urls import patterns, include, url
from django.contrib import admin

from djangoschool import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/$', views.ICSView.as_view(), name='calendar'),
    url(r'^$', views.IndexView.as_view(), name='home'),
)
