from django.contrib import admin

from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'complete_before ', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ['name']}