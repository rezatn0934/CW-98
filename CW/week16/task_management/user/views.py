from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.views import View

from .forms import LoginForm, UserForm, ChangePassForm
from .mixins import ProfileMixin
from .models import CustomUser
from .authentication import AuthBackend


def user_login(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = cd['user']
            login(request, user, backend='user.authentication.AuthBackend')
            return redirect('/')
        message = "Invalid login credentials"
    elif request.method == "GET":
        form = LoginForm()
    return render(request, "user/login.html", {"message": message, "form": form})


def register_user(request):
    message = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='user.authentication.AuthBackend')
            return redirect('/')
    elif request.method == "GET":
        form = UserForm()
    return render(request, "user/login.html", {"message": message, "form": form})


class ProfileView(ProfileMixin, View):
    temp_name = 'user/profile.html'


def log_out(request):
    logout(request)
    return redirect('login')
