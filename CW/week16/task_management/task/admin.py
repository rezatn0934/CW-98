from django.contrib import admin
from django.contrib import messages
from django.http.response import JsonResponse
from .models import Task, Category, Tag
# Register your models here.

import csv
import json


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    actions = ['export_to_csv', 'export_to_json']
    readonly_fields = ('is_active',)
    list_display = ('title', 'due_date', 'user', 'status', 'category', 'is_active', 'created', 'updated', 'description')
    list_editable = ('status',)
    list_filter = ('status', 'category')
    search_fields = ('title', 'category__name')

    @admin.action(description='Export To csv')
    def export_to_csv(self, request, queryset):
        header = ['title', 'due_date', 'status', 'category', 'tag', 'user', 'created',
                  'updated', 'is_active']
        with open('task/task.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for item in queryset:
                writer.writerow(
                    [item.title, item.due_date, item.status, item.category, item.tag, item.user, item.created,
                     item.updated, item.is_active])

        messages.success(request, 'CSV file for selected model has been successfully created at task/task.csv')

    @admin.action(description='Export To Json')
    def export_as_json(self, request, queryset):
        meta = self.model._meta

        data = list(queryset.values())
        response = JsonResponse(data, safe=False)
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(meta)
        return response


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('label',)
