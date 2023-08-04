from django import forms
from .models import Task, Tag, Category


class CreatTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateTaskForm(forms.Form):
    title = forms.CharField()
    due_date = forms.DateField()
    description = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())


class CreateCategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'text-align: center;'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Description', 'style': 'text-align: center;'}))


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
        model = Tag
        fields = ('label',)
        widgets = {
            'label': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Label', 'style': 'text-align: center;'})
        }
