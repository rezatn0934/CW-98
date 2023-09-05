from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AbstractUser, Artist, Listener
from .forms import ArtistRegisterForm, CustomUserCreationForm, CustomUserChangeForm

admin.site.site_header = 'Music Player Management'
admin.site.site_title = 'Colorlib Management'
admin.site.index_title = 'Welcome to admin panel'


@admin.register(AbstractUser)
class AbstractUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = [
        [None, {'fields': ['username', 'email', 'password1', 'password2']}],
        ['Personal Info', {'fields': ['name', ]}],
        ['Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}],
    ]
    add_fieldsets = [
        [None, {'fields': ['username', 'email', 'password1', 'password2']}],
        ['Personal Info', {'fields': ['name', ]}],
        ['Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}],
    ]
    list_display = ['username', 'email', 'name', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'name']
    ordering = ['username', ]

