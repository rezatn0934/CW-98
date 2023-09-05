from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('like/', views.LikeView.as_view(), name='like'),
    path('create_comment/', views.CreatCommentView.as_view(), name='create_comment'),
]
