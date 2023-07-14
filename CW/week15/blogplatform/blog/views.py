from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def view_home(request):
    return render(request, 'blog/home.html')


def view_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


def view_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def view_category(request):
    categorys = Category.objects.all()
    return render(request, 'blog/category.html', {'categorys': categorys})
