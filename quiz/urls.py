from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns =[
    path('', views.welcome, name='welcome'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('saveans', views.saveans, name='saveans')
    
]