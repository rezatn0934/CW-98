from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Comment


class CommentCreation(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

