from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


class TodoMixin:
    form_class = TodoForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        if not todo.user == request.user:
            return redirect('permision')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        todo = Todo.objects.filter(id=pk)
        todo = todo.get(id=pk)
        form = self.form_class(instance=todo)
        return render(request, self.template_name, {'todo': todo, 'form': form})

    def post(self, request, pk):
        todo1 = Todo.objects.get(id=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = todo1.user
            todo.save()
            return redirect('thank_you', todo.id)
        return render(request, self.template_name, {'todo': todo})
