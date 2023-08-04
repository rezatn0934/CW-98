from django import forms
from .models import Task, Tag, Category


class CreatTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'text-align: center;'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description', 'style': 'text-align: center;'}),
        }


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'label'
        widgets = {
            'label': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'text-align: center;'})
        }
