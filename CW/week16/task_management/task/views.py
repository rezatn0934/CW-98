from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Task, Category, Tag


# Create your views here.


def home_view(request):
    tasks = Task.objects.all().order_by('due_date')

    first_task = tasks[0]

    paginator = Paginator(tasks[1:], 6)
    page_number = request.GET.get('page', 1)
    tasks = paginator.get_page(page_number)
    context = {'tasks': tasks, 'first_task': first_task}

    return render(request, 'task/home.html', context)


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
    elif request.method == 'POST':
        task_title = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        status = request.POST.get('status')
        category = get_object_or_404(Category, pk=request.POST.get('category'))
        due_date = request.POST.get('due_date')
        task = Task.objects.create(title=task_title, description=task_description, category=category, status=status, due_date=due_date)
        tag_ids = map(int, request.POST.getlist('tags'))
        tags = Tag.objects.filter(id__in=tag_ids)
        for tag in tags:
            task.tag.add(tag)
        return redirect(request.path)


def tasks_tale_view(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
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
        }
        return render(request, 'task/task_detail.html', context)
    elif request.method == 'POST':
        print(request.POST)
        if 'create_tag' in request.POST:
            tas_label = request.POST.get('tag_label')
            Tag.objects.create(label=tas_label)
            return redirect(request.path)
        elif 'update_task' in request.POST:
            task = get_object_or_404(Task, pk=pk)
            task.title = request.POST.get('task_name')
            task.description = request.POST.get('task_description')
            task.status = request.POST.get('status')
            task.category = get_object_or_404(Category, pk=request.POST.get('category'))
            task.due_date = request.POST.get('due_date')
            task.save()
            task.tag.clear()
            tag_ids = map(int, request.POST.getlist('tags'))
            tags = Tag.objects.filter(id__in=tag_ids)
            for tag in tags:
                task.tag.add(tag)
            return redirect(request.path)


def task_search_view(request):
    search_query = request.GET.get('search')
    checkbox = request.GET.getlist('checkbox')
    if search_query:
        if ('a' in checkbox) and ('b' in checkbox) and ('c' in checkbox):
            search_results = Task.objects.filter(
                Q(title__icontains=search_query) | Q(tag__label__icontains=search_query) | Q(description__icontains=search_query)).distinct()
        elif ('a' in checkbox) and ('b' in checkbox) and not ('c' in checkbox):
            search_results = Task.objects.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)).distinct()
        elif ('a' in checkbox) and ('c' in checkbox) and not ('b' in checkbox):
            search_results = Task.objects.filter(
                Q(title__icontains=search_query) | Q(tag__label__icontains=search_query)).distinct()
        elif ('b' in checkbox) and ('c' in checkbox) and not ('a' in checkbox):
            search_results = Task.objects.filter(
                Q(description__icontains=search_query) | Q(tag__label__icontains=search_query)).distinct()
        else:
            search_results = Task.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(tag__label__icontains=search_query)).distinct()

        paginator = Paginator(search_results, 3)
        page_number = request.GET.get('page', 1)
        search_results = paginator.get_page(page_number)
    else:
        search_results = None
    return render(request, 'task/search.html', {'search_query': search_query, 'search_results': search_results})


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'task/category.html', context)
    elif request.method == 'POST':
        categories_name = request.POST.get('category_name')
        categories_description = request.POST.get('category_description')
        Category.objects.create(name=categories_name, description=categories_description)
        return redirect(request.path)


def category_detail_view(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET':
        tasks = Task.objects.filter(category=category)
        paginator = Paginator(tasks, 3)
        page_number = request.GET.get('page', 1)
        tasks = paginator.get_page(page_number)
        context = {'category': category, 'tasks': tasks}
        return render(request, 'task/category_details.html', context)
    elif request.method == 'POST':
        category.name = request.POST.get('category_name')
        category.description = request.POST.get('category_description')
        category.save()
        return redirect(request.path)

