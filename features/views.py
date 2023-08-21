from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'Register.html')


def create_question(request):
    return render(request, 'createQuestions.html')


def question_details(request):
    return render(request, 'question_info.html')
