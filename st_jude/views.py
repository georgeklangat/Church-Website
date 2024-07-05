from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from django.http import HttpResponseRedirect
# from .forms import RegisterForm

from .models import *


def home(request):
    activities = Activity.objects.all()
    # print(activities)  # This should print the QuerySet in the console
    return render(request, 'STJUDE_WEB.html', {'activities': activities})


#
#
# def signup(request):
#     return render(request, 'sign_up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'invalid credentials!!!')
            return redirect('login')
    else:
        return render(request, 'log_in.html')


def homepage(request):
    return render(request, 'home_page.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        registration_no = request.POST['registration_no']
        email = request.POST['email']
        # course = request.POST['course']
        # jumuiya = request.POST['jumuiya']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                return redirect('login')
        else:
            messages.info(request, "Password Not matching...")
            return redirect('register')

    else:
        return render(request, 'sign_up.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


# def registration(request):
#     submitted = False
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect('/registration?submitted')
#     else:
#         form = RegisterForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'Register.html', {'form': form, 'submitted': submitted})

