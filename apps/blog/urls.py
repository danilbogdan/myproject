from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogView.as_view(), name='blog'),
    url(r'^post/(?P<slug>[-\w]+)$', views.PostView.as_view(), name='post'),
    url(r'^add_post/$', views.AddPostView.as_view(), name='add_post'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    url(r'^services/$', views.ServicesView.as_view(), name='services'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
