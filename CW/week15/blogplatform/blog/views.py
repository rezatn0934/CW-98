from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def view_home(request):
    return render(request, 'blog/home.html')


def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


def view_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def view_categorys(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'blog/category.html', context)


def view_category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    context = {'category': category}
    return render(request, 'blog/category_detail.html', context)