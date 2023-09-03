from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

from .forms import ArtistRegisterForm, ListenerRegisterForm, LoginForm


# Create your views here.


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm
    next_page = reverse_lazy('song:home')

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)
