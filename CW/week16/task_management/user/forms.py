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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if not password or not password2 or password != password2:
            raise forms.ValidationError("Passwords do not match.")
        del cleaned_data['password2']
        return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'text-align: center;'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'text-align: center;'}),
        }

    def clean(self):
        cleaned_data = {'username': self['username'].value(), 'password': self['password'].value()}
        username1 = cleaned_data["username"]
        user = CustomUser.objects.filter(Q(username=username1) | Q(email=username1)).get()

        if user.check_password(cleaned_data['password']):
            cleaned_data['user'] = user
            return cleaned_data


class UpdateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'image')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'text-align: center;'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name', 'style': 'text-align: center;'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name', 'style': 'text-align: center;'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'text-align: center;'}),
            'image': forms.FileInput(
                attrs={'class': 'form-control', 'name': 'image'}
            )
        }
        help_texts = {'username': None}


class ChangePassForm(forms.Form):
    old_password = forms.CharField(required=True, label='old_password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'old_password', 'style': 'text-align: center;'}))
    password1 = forms.CharField(required=True, label='password1', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password1', 'style': 'text-align: center;'}))
    password2 = forms.CharField(required=True, label='password2', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password2', 'style': 'text-align: center;'}))
