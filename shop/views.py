from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import Signup


def shop(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})


def about(request):
    return render(request, 'about us.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('با موفقیت وارد شدید'))
            return redirect("home")
        else:
            messages.success(request, ('نام کاربری یا گذرواژه شما نادرست است'))
            return redirect("signup")
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('با موفقیت خارج شدید'))
    return redirect("home")


def signup_user(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get("username"))

            login(request, user)
            messages.success(request, ('اکانت شما با موفقیت ساخته شد'))
            return redirect("home")




    return render(request, 'signup.html', {'form': form})


