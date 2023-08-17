from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView, FormView, CreateView
from django.views import View
from django.urls import reverse_lazy
from .models import Task, Category, Tag
from .forms import CreatTaskForm, UpdateTaskForm, CreateCategoryForm, UpdateCategoryForm, CreateTagForm
from .mixins import TodoOwnerRequiredMixin


# Create your views here.


class HomeView(ListView):
    template_name = 'task/home.html'
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['tasks'] = self.model.objects.filter(user=self.request.user).order_by('due_date').distinct()
        else:
            context['tasks'] = None

        if context['tasks']:
            context['first_task'] = context['tasks'][0]
        else:
            context['first_task'] = None
        return context


def all_seeing_eye_view(request):
    if request.method == 'GET':
        sort = request.GET.get('sort', 'title')
        order = request.GET.get('order', 'asc')
        if sort == 'title' or sort == 'status' or sort == 'due_date':
            sort_param = sort if order == 'asc' else '-' + sort
            tasks = Task.objects.order_by(sort_param)
            stats = []
            status_label = []
            for i in Task.STATUS_CHOICES:
                status_label.append(i[0])
                stats.append(i[0])
            tags = Tag.objects.all()
            categories = Category.objects.all()
        else:
            tasks = Task.objects.all()
            stats = []
            status_label = []
            for i in Task.STATUS_CHOICES:
                status_label.append(i[0])
                stats.append(i[0])
            tags = Tag.objects.all()
            categories = Category.objects.all()

        paginator = Paginator(tasks, 5)
        page_number = request.GET.get('page', 1)
        tasks = paginator.get_page(page_number)

        context = {
            'tasks': tasks,
            'order': 'desc' if order == 'asc' else 'asc',
            'sort': sort,
            'page': page_number,
            'tags': list(tags),
            'stats': stats,
            'categories': categories,
        }
        return render(request, 'task/tasks_list.html', context)


class CreateTask(CreateView):
    template_name = 'task/creat_task.html'
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'category', 'tag']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form)


class UpdateTask(UpdateView):
    template_name = 'task/creat_task.html'
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'category', 'tag']
    success_url = reverse_lazy('task_list')


class TaskDetail(TodoOwnerRequiredMixin, View):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form1 = CreateTagForm()
        form2 = UpdateTaskForm(initial={
            'title': task.title,
            'due_date': task.due_date,
            'description': task.description,
            'category': task.category,
            'tag': task.tag.all(),
        })
        stats = []
        status_label = []
        for i in Task.STATUS_CHOICES:
            status_label.append(i[0])
            stats.append(i[0])
        tags = Tag.objects.all()
        categories = Category.objects.all()
        context = {
            'task': task,
            'tags': list(tags),
            'stats': stats,
            'categories': categories,
            'form1': form1,
            'form2': form2
        }
        return render(request, 'task/task_detail.html', context)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if 'create_tag' in request.POST:
            form = CreateTagForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('task_detail', pk=pk)
        elif 'update_task' in request.POST:
            form = UpdateTaskForm(request.POST)
            if form.is_valid():
                task.title = form.cleaned_data['title']
                task.due_date = form.cleaned_data['due_date']
                task.description = form.cleaned_data['description']
                task.category = form.cleaned_data['category']
                task.tag.set(form.cleaned_data['tag'])
                task.save()
                return redirect('task_detail', pk=task.id)


def task_search_view(request):
    search_query = request.GET.get('search')
    checkbox = request.GET.getlist('checkbox')
    if request.method == 'GET':
        if search_query:
            query_list = []

            if 'a' in checkbox:
                query_list.append(Q(name__icontains=search_query))
            if 'b' in checkbox:
                query_list.append(Q(description__icontains=search_query))
            if 'c' in checkbox:
                query_list.append(Q(category__name__icontains=search_query))

            if not query_list:
                query_list.append(Q(name__icontains=search_query) |
                                  Q(description__icontains=search_query) |
                                  Q(category__name__icontains=search_query))

            search_results = Task.objects.filter(*query_list).distinct()
            paginator = Paginator(search_results, 3)
            page_number = request.GET.get('page', 1)
            search_results = paginator.get_page(page_number)
        else:
            search_results = None
    else:
        search_results = None
    return render(request, 'task/search.html', {'search_query': search_query, 'search_results': search_results})


class CategoryView(FormView):
    model = Category
    template_name = 'task/category.html'
    form_class = CreateCategoryForm
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        category = self.model.objects.create(name=name, description=description)
        return redirect('category_detail', pk=category.id)


def category_detail_view(request, pk):
    category = Category.objects.get(pk=pk)
    tasks = Task.objects.filter(category=category)
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page', 1)
    tasks = paginator.get_page(page_number)
    if request.method == 'GET':
        form = UpdateCategoryForm(instance=category)
        context = {'category': category, 'tasks': tasks, 'form': form}
        return render(request, 'task/category_details.html', context)
    elif request.method == 'POST':
        form = UpdateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('category_detail', pk=category.id)
