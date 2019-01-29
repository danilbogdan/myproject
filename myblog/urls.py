"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^accounts/login/$', login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('apps.blog.urls')),]
