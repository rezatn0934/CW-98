

from django.contrib import admin
from django.urls import path
from .views import view_home, view_posts, view_post_detail, view_categorys, view_category_detail


urlpatterns = [
    path('', view_home, name='home'),
    path('posts/', view_posts, name='posts'),
    path('post/<int:pk>/', view_post_detail, name='post_detail'),
    path('categorys/', view_categorys, name='categorys'),
    path('category/<int:pk>/', view_category_detail, name='category_detail'),
]
