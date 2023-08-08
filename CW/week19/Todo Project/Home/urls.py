from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('todos/', views.TodoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todos/<int:pk>', views.TankYou.as_view(), name='thank_you')
]
