from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.register_user, name='register'),
    path('change_pass/', views.ChangePassView.as_view(), name='change_pass'),
    path('logout/', views.log_out, name='logout')
]
