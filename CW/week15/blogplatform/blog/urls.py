

from django.contrib import admin
from django.urls import path
from .views import view_home, view_post, view_post_detail


urlpatterns = [
    path('', view_home),
    path('post/', view_post),
    path('post/<int:pk>/', view_post_detail, name='post_detail'),
]