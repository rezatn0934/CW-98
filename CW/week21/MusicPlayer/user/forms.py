from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Artist, Listener, Band, AbstractUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AbstractUser
        fields = '__all__'
