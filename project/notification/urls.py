from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^show/(?P<notification_id>\d+)/$','notification.views.show_notification'),
    url(r'^delete/(?P<notification_id>\d+)/$','notification.views.delete_notification'),
)
