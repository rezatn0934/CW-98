from django.shortcuts import render
from .models import Author
# Create your views here.

def view_author(request):
    authors = Author.objects.all()
    return render(request, 'blog/author.html', {'poauthorssts': authors})
