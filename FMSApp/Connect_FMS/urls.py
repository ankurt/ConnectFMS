from django.conf.urls import patterns, include, url
from django.contrib import admin
from Connect_FMS import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.login, name='login'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^feed/$', views.index, name='feed'),
    url(r'^(?P<post_id>\d+)/$', views.details, name='details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form_upload',views.post_form_upload, name='post_form_upload')
    # url(r'^like(?P<post_id>\d+)$', views.vote, name='like')
)
