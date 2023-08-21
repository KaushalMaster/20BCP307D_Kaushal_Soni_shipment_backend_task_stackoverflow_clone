from django.shortcuts import render, redirect
from .models import register_user
import random
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    five_digit_random = random.randrange(10000, 100000)
    print("5-Digit Random Number:", five_digit_random)
    if request.method == "POST":
        user_id = five_digit_random
        email = request.POST['email']
        password = request.POST['password']

        print(user_id, email, password)
        login = login(user_id, email, password)
        login.save()
        return redirect(request, 'index.html')
        # Check if a user with the same username already exists
        # if register_user.objects.filter(user_email=email).exists():
        #     # Check if the password is correct
        #     if register_user.objects.filter(user_password=password).exists():
        #         # Login successful
        #         return render(request, 'index.html')
        #     else:
        #         # Login failed
        #         messages.error(request, 'Incorrect password.')
        # else:
        #     # Login failed
        #     messages.error(request, 'User does not exist.')
    return render(request, 'login.html')


def register(request):
    # Generates a random number between 1 and 100 (inclusive)
    # Generates a random number between 10000 and 99999
    five_digit_random = random.randrange(10000, 100000)
    print("5-Digit Random Number:", five_digit_random)
    if request.method == "POST":
        user_id = five_digit_random
        name = request.POST['display_name']
        email = request.POST['email']
        password = request.POST['password']

        ans = register_user(user_id, name, email, password)
        if ans.save():
            messages.success(
                request, 'Registration successful! You can now log in.')
        print(five_digit_random, name, email, password)

    return render(request, 'Register.html')

# def register(request):
#     if request.method == "POST":
#         name = request.POST['display_name']
#         email = request.POST['email']
#         password = request.POST['password']

#         # Check if a user with the same username already exists
#         if register_user.objects.filter(user_name=name).exists():
#             messages.error(
#                 request, 'Username already exists. Please choose a different username.')
#         else:
#             # Generate a random user_id (you can modify this part if needed)
#             user_id = random.randint(10000, 99999)

#             # Create and save the new user
#             new_user = register_user(
#                 user_id=user_id, user_name=name, user_email=email, user_password=password)

#             new_user.save()

#             messages.success(
#                 request, 'Registration successful! You can now log in.')

#     return render(request, 'Register.html')


def create_question(request):
    return render(request, 'createQuestions.html')


def question_details(request):
    return render(request, 'question_info.html')
