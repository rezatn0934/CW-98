from django import forms
from .models import Task, Tag, Category


class CreatTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
