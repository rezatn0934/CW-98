from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import View
from .models import Task, Category, Tag
from .forms import CreatTaskForm, UpdateTaskForm, CreateCategoryForm, UpdateCategoryForm, CreateTagForm


# Create your views here.

class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['pk'])
        if not request.user.is_authenticated or not task.user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def home_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('due_date').distinct()
    else:
        tasks = Task.objects.all().order_by('due_date')
    if tasks:
        first_task = tasks[0]
    else:
        first_task = None

    paginator = Paginator(tasks[1:], 6)
    page_number = request.GET.get('page', 1)
    tasks = paginator.get_page(page_number)
    context = {'tasks': tasks, 'first_task': first_task}

    return render(request, 'task/home.html', context)


def all_seeing_eye_view(request):
    if request.method == 'GET':
        sort = request.GET.get('sort', 'title')
        order = request.GET.get('order', 'asc')
        form = CreatTaskForm()
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
            'form': form
        }
        return render(request, 'task/tasks_list.html', context)
    elif request.method == 'POST':
        form = CreatTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', task_id=task.id)


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

    def post(self, request, task):
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


def categories_view(request):
    if request.method == 'GET':
        form = CreateCategoryForm()
        categories = Category.objects.all()
        context = {'categories': categories, 'form': form}
        return render(request, 'task/category.html', context)
    elif request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = Category.objects.create(name=name, description=description)
            return redirect('category_detail', category_id=category.id)


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

