from django.contrib import admin
from .models import Task, Category, Tag
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'user', 'status', 'category', 'created', 'updated', 'description')
    list_editable = ('status',)
    list_filter = ('status', 'category')
    search_fields = ('title', 'category__name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('label',)
