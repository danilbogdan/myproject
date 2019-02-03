from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogView.as_view(), name='blog'),
    url(r'^post/(?P<slug>[-\w]+)$', views.PostView.as_view(), name='post'),
    url(r'^add_post/$', views.AddPostView.as_view(), name='add_post'),
]
