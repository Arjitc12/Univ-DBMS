from django.conf.urls import url
from django.contrib import admin

from . import views
from django.http import HttpResponse
from django.shortcuts import render

from .views import Home_View

urlpatterns = [
    # url('', views.Home_View,name='Home'),
    url(r'^home/', Home_View, name='Home'),
   # url(r'^register/', UserFormView.as_view(), name='Register'),
    url(r'^admin/', admin.site.urls),
    # url(r'^register/', views.UserFormView.as_view(), name='register'),
]
