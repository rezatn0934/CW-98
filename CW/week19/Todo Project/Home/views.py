from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from .mixins import TodoMixin


class IndexView(View):
    def get(self, request):

        return render(request, 'Home/index.html')



        return render(request, 'todo_list.html', {'todos': todos})


class TodoDetailView(TodoMixin, View):
    template_name = 'todo_detail.html'



        return render(request, 'Home/todo_list.html', {'todos': todos})


class TodoDetailView(TodoMixin, View):
    template_name = 'Home/todo_detail.html'


class TankYou(View):
    def get(self, request, pk):
        return redirect(request, pk)


def permision(request):
    return render(request, 'Home/permision_denied.html')
