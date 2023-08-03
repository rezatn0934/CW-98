from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser


# Create your views here.


def user_login(request):
    message = None
    if request.method == "POST":
        print('20' * 100)
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            print(type(user))
            print(user.username)
            # user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                print('1' * 100)
                login(request, user)
                return render(request, 'user/dashboard.html', {'user': user})
            else:
                message = "Invalid phone number or password"
    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
    form = LoginForm()
    return render(request, "user/login.html", {"message": message, "form": form})
