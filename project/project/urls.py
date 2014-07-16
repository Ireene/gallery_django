from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gallery.views.albums'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^notification/', include('notification.urls')),
    url(r'^galleries/', include('gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                    'document_root': settings.MEDIA_ROOT,
                }),    
     # user auths urls
    url(r'^accounts/login/$', 'project.views.login'),
    url(r'^accounts/auth/$', 'project.views.auth_view'),
    url(r'^accounts/logout/$', 'project.views.logout'),
    url(r'^accounts/loggedin/$', 'project.views.loggedin'),
    url(r'^accounts/invalid/$', 'project.views.invalid_login'),
    
    # user registration
    url(r'^accounts/register/$', 'project.views.register_user'),
    url(r'^accounts/register_success/$', 'project.views.register_success'),
)
