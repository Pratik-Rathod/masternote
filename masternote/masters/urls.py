from . import views
from django.urls import path
urlpatterns = [
    path('',name='home',view=views.home),
    path('login',name='login',view=views.userlogin),
    path('logout',name='logout',view=views.userlogout),
]