from django.contrib import admin
from django import forms
from .models import CustomUser


# Register your models here.

admin.site.register(CustomUser)
