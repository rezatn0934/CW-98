from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View
import logging
from .forms import ArtistRegisterForm, ListenerRegisterForm, LoginForm
from .models import AbstractUser

logger = logging.getLogger('django')


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
        user_name = self.request.POST.get('username')
        try:
            user = AbstractUser.objects.get(username=user_name)
        except Exception as e:
            user = AbstractUser.objects.get(email=user_name)

        logger.info(f"User {user.username} logged in")
        return super().form_valid(form)


class UserRegisterView(View):
    redirect_authenticated_user = True
    template_name = 'user/register.html'

    def get(self, request):
        artist_form = ArtistRegisterForm()
        listener_form = ListenerRegisterForm()
        return render(request, self.template_name, {'artist_form': artist_form, 'listener_form': listener_form})

    def post(self, request):
        user_type = request.POST.get('user')
        form = None
        if user_type == 'artist':
            form = ArtistRegisterForm(request.POST)
        elif user_type == 'listener':
            form = ListenerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user_type == 'artist':
                group_name = 'VIP'
                group = Group.objects.get(name=group_name)
                user.groups.add(group)

            login(request, user, backend='user.authentication.AuthBackend')
            subject = 'Welcome'
            message = 'Welcome to our website.'
            recipient_list = [user.email, ]
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, recipient_list)

            logger.info(f"New user registered: {user.username}")

            return redirect(reverse('song:home'))

        artist_form = ArtistRegisterForm()
        listener_form = ListenerRegisterForm()
        messages.error(request, form.errors)
        return render(request, self.template_name, {'artist_form': artist_form, 'listener_form': listener_form})
