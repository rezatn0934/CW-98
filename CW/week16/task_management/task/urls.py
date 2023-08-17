from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('tasks/', views.all_seeing_eye_view, name="task_list"),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('search/', views.task_search_view, name='search'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
    path('category/<int:pk>/', views.category_detail_view, name='category_detail'),
]