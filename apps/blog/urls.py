from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogView.as_view(), name='blog'),
    url(r'^post/$', views.PostView.as_view(), name='post')
]
