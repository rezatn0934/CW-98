from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('todos/', views.TodoListView, name='todo_list'),
    path('todos/<int:pk>/', views.TodoDetailView, name='todo_detail'),
]
