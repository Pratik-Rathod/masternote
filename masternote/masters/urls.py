from . import views
from django.urls import path
urlpatterns = [
    path('',name='home',view=views.home),
    path('login',name='login',view=views.user_login),
    path('logout',name='logout',view=views.user_logout),
    path('register',name='register',view=views.user_register),
]