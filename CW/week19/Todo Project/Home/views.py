from django.shortcuts import render
from django.views import View
from .models import Todo
from .mixins import TodoMixin


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'todo_list.html', {'todos': todos})


class TodoDetailView(TodoMixin, View):
    template_name = 'todo_detail.html'


