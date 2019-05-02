from django.contrib import admin
from django.urls import path, include
from .views import task_list_list,task_list_detail , task_list, task_detail, Register
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('task_list/', task_list_list.as_view()),
    path('task_list/<int:pk>/', task_list_detail.as_view()),
    path('task_list/<int:pk>/tasks/', task_list),
    path('tasks/<int:pk>/', task_detail),
    path('register/', Register.as_view()),
    path('login/', obtain_jwt_token),

]
