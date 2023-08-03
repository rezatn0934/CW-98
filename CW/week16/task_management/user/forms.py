from django import forms
from .models import CustomUser


class CreatUserForm(forms.ModelForm):
    class Meta:
        Model = CustomUser
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        Model = CustomUser
        fields = ('username', 'password')
