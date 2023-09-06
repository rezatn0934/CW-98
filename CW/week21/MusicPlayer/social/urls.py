from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('like/', views.LikeView.as_view(), name='like'),
    path('create_comment/', views.CreatCommentView.as_view(), name='create_comment'),
    path('update_playlist/', views.UpdatePlayListView.as_view(), name='update_playlist'),
    path('create_playlist/', views.CreatPlayListView.as_view(), name='create_playlist'),
]
