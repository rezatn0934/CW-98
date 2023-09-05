from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Artist, Listener, Band, AbstractUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AbstractUser
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password1', 'type': 'password', 'name': 'password1',
               'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2', 'type': 'password', 'name': 'password2',
               'placeholder': 'Password'}))

    class Meta:
        model = AbstractUser
        fields = ('username', 'email', 'name', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email address',
            'name': 'Name',
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'exampleInputUser', 'aria-describedby': 'usernameHelp',
                       'placeholder': "Username"}
            ),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'exampleInputName', 'placeholder': "Enter a Name"}
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                       'placeholder': "Enter E-mail"}
            ),
        }


class ArtistRegisterForm(CustomUserCreationForm):
    bio = forms.CharField(required=False, label="Bio",
                          widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your bio'}))
    band = forms.ModelChoiceField(queryset=Band.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}), label="Band",
                                  required=False)

    class Meta(CustomUserCreationForm.Meta):
        model = Artist
        fields = ('username', 'email', 'name', 'bio', 'band', 'image', 'password1', 'password2')


class ListenerRegisterForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = Listener
        fields = ('username', 'email', 'name', 'image', 'password1', 'password2')


