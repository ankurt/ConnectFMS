from django.conf.urls import patterns, include, url
from django.contrib import admin
from FMSApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FMSApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
)
