from os import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
]