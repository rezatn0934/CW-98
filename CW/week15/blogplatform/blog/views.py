from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def home_view(request):
    return render(request, 'blog/home.html')


def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/category.html', context)


def category_detail_view(request, pk):
    category = Category.objects.get(pk=pk)
    context = {'category': category}
    return render(request, 'blog/category_detail.html', context)