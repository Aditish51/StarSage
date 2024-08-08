
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_quiz, name= 'home_quiz'),
    path('levels/', views.levels, name= 'levels'),
    path('bq/', views.basic_ques, name= 'basic_ques'),
    path('nq/', views.next_ques, name= 'next_ques'),
]
