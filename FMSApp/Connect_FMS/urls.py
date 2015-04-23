from django.conf.urls import patterns, include, url
from django.contrib import admin
from Connect_FMS import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.login, name='login'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^feed/$', views.index, name='feed'),
    url(r'^(?P<post_id>\d+)/$', views.details, name='details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form_upload',views.post_form_upload, name='post_form_upload'),
    url(r'^register', views.register, name='register'),
    url(r'^about', views.about, name='about'),
    url(r'^signup', views.register, name='signup'),
    url(r'^submit-comment', views.submit_comment, name='submit_comment'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
