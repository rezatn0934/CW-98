from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from django import forms
from .models import CustomUser


class IsGreatUserFilter(admin.SimpleListFilter):
    title = 'is_great_user'
    parameter_name = 'is_great_user'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(task_count__gt=10)
        elif value == 'No':
            return queryset.exclude(task_count__gt=10)
        return queryset
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_great_user', 'task_count', 'first_name', 'last_name', 'email', 'is_staff',
                    'is_active', 'is_superuser', 'img_preview'];
    ordering = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', ]
    fields = [IsGreatUserFilter]

    @admin.display(ordering='task_count')
    def task_count(self, user):
        url = (reverse('admin:task_task_changelist')
               + '?'
               + urlencode({
                    'user__id': str(user.id)
                }))

        return format_html('<a href="{}">{}</a>', url, user.task_count)

    task_count.short_description = 'Number Of Tasks'

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            task_count=Count('task__user')
        )

    def is_great_user(self, obj):
        if obj.task_count > 10:
            return True
        else:
            return False
