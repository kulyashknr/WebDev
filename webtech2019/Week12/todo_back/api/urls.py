from django.contrib import admin
from django.urls import path, include
from .views import TaskListListCreate, TaskListDetailUpdateDelete, TaskListCreate, TaskDetailUpdateDelete

urlpatterns = [
    path('task_list/', TaskListListCreate.as_view()),
    path('task_list/<int:pk>/', TaskListDetailUpdateDelete.as_view()),
    path('task_list/<int:pk>/tasks/', TaskListCreate.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDelete.as_view())
]
