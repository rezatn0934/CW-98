from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from django import forms
from .models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_great_user', 'task_count', 'first_name', 'last_name', 'email', 'is_staff',
                    'is_active', 'is_superuser', 'img_preview'];
    ordering = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', ]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            task_count=Count('task__user')
        )
