from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('tasks/', views.all_seeing_eye_view, name="task_list"),
    path('task_detail/<int:pk>/', views.tasks_tale_view, name='task_detail'),
    path('search/', views.task_search_view, name='search'),
    path('categories/', views.categories_view, name='categories'),
    path('category/<int:pk>/', views.category_detail_view, name='category_detail'),
]