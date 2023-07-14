

from django.contrib import admin
from django.urls import path
from .views import view_home, view_post, view_post_detail, view_category, view_category_detail


urlpatterns = [
    path('', view_home),
    path('post/', view_post, name='post'),
    path('post/<int:pk>/', view_post_detail, name='post_detail'),
    path('category/', view_category, name='category'),
    path('category/<int:pk>/', view_category_detail, name='category_detail'),
]
