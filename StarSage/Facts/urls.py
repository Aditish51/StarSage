
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_facts, name= 'home_facts'),
]