from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .models import CustomUser


class UserForm(forms.ModelForm):
    password2 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'text-align: center;'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'text-align: center;'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name', 'style': 'text-align: center;'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name', 'style': 'text-align: center;'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'text-align: center;'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'text-align: center;'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
