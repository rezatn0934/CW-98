from django.urls import path
from .views import view_authors, view_author_detail


urlpatterns = [
    path('authors/', view_authors, name='authors'),
    path('author/<int:pk>/', view_author_detail, name='author_detail'),
]
