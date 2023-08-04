from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, UserForm
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


