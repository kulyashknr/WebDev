from django.contrib import admin
from .models import TaskList, Task


class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')
    list_display_links = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')


admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)