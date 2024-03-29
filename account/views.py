from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'account/signup_user.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todos')
            except IntegrityError:
                return render(request, 'account/signup_user.html',
                              {'form': UserCreationForm, 'error': 'Это имя пользователя уже занято.'})

        else:
            return render(request, 'account/signup_user.html',
                          {'form': UserCreationForm, 'error': 'Пароли не совпадают. Попробуйте еще раз.'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'account/login_user.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Пароль или имя пользователя не совпадают'})
        else:
            login(request, user)
            return redirect('current_todos')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
