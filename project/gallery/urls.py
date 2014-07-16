from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^albums/$', 'gallery.views.albums'),
    url(r'^create_image/$', 'gallery.views.create_image'),
    url(r'^create_album/$', 'gallery.views.create_album'),
    url(r'^get/(?P<album_id>\d+)/$', 'gallery.views.album'),
    url(r'^show_image/(?P<image_id>\d+)/$', 'gallery.views.show_image'),
    url(r'^delete_image/(?P<image_id>\d+)/$', 'gallery.views.delete_image'),
    url(r'^delete_image/(?P<image_id>\d+)/$', 'gallery.views.delete_image'),
    url(r'^add_comment/(?P<image_id>\d+)', 'gallery.views.add_comment'),
)
