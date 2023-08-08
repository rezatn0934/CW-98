from django import forms
from .models import Todo


class TodoForm(forms.Form):
    class Meta:
        model = Todo
        fields = ['user', 'title', 'description', 'is_completed']

