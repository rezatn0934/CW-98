from django.shortcuts import render
from .models import Author
# Create your views here.

def view_authors(request):
    authors = Author.objects.all()
    return render(request, 'user/author.html', {'authors': authors})


def view_author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'user/author_detail.html', {'author': author})
