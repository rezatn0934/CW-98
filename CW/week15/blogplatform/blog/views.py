from django.shortcuts import render
from .models import Post
# Create your views here.


def view_home(request):
    return render(request, 'blog/home.html')


def view_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})
