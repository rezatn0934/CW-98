from django import forms
from .models import CustomUser


class CreatUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
