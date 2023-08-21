from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('create_question', views.create_question, name='create_question'),
    path('question_details', views.question_details, name='question_details')
]
