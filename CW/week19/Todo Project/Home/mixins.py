from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


class TodoMixin:
    form_class = TodoForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['id'])
        if not todo.user == request.user:
            raise PermissionDenied

    def get(self, request, id):
        todo = Todo.objects.filter(id=id)
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
