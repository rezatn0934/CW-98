from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Task, Category


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
    sort = request.GET.get('sort', 'title')
    order = request.GET.get('order', 'asc')
    if sort == 'title' or sort == 'status' or sort == 'due_date':
        sort_param = sort if order == 'asc' else '-' + sort
        tasks = Task.objects.order_by(sort_param)
    else:
        tasks = Task.objects.all()

    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page', 1)
    tasks = paginator.get_page(page_number)

    context = {
        'tasks': tasks,
        'order': 'desc' if order == 'asc' else 'asc',
        'sort': sort,
        'page': page_number
    }
    return render(request, 'task/tasks_list.html', context)


def tasks_tale_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task/task_detail.html', context)


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
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'task/category.html', context)


def category_detail_view(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        tasks = Task.objects.filter(category=category)
        paginator = Paginator(tasks, 3)
        page_number = request.GET.get('page', 1)
        tasks = paginator.get_page(page_number)
        context = {'category': category, 'tasks': tasks}
    elif request.method == 'POST':
        categories_name = request.POST.get('category_name')
        categories_description = request.POST.get('category_description')
        Category.objects.create(name=categories_name, description=categories_description)
        return redirect('category_detail', pk=pk)

    return render(request, 'task/category_details.html', context)
