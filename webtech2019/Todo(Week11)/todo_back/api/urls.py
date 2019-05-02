from django.contrib import admin
from django.urls import path, include
from .views import task_list_list, task_list_detail, task_list, task_detail

urlpatterns = [
    path('task_list/', task_list_list),
    path('task_list/<int:pk>', task_list_detail),
    path('task_list/<int:pk>/tasks/', task_list),
    path('tasks/<int:pk>/', task_detail)
]
