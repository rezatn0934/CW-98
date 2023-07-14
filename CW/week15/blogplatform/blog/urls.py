

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.posts_view, name='posts'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('categories/', views.categories_view, name='categories'),
    path('category/<int:pk>/', views.category_detail_view, name='category_detail'),
]
