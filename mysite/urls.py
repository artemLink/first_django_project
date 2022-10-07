from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('mail', views.mail),
    path('users', views.users),
    path('send_msg', views.send_msg)
]