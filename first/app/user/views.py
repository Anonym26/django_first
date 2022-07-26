from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect

from app.user.forms import RegistrationForm, LoginForm


def create_user(request):
    """Создает нового пользователя"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User(**form.cleaned_data)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

        return redirect('main')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'user/registration.html', context=context)


def login_user(request):
    """Авторизует пользователя"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('main')
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'user/login.html', context=context)


def logout_user(request):
    """Выходит из авторизации"""
    auth.logout(request)
    return redirect('main')
