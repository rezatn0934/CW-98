from django.contrib import admin
from django import forms
from .models import CustomUser


# Register your models here.


class CreateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
