from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register')
]