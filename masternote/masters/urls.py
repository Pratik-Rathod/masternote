from . import views
from django.urls import path
urlpatterns = [
    path('',name='test',view=views.test),
]