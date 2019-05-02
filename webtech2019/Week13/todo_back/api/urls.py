from django.urls import path
from .views.views_cbv import TaskListListCreate, TaskListDetailUpdateDelete, TaskListCreate, \
    TaskDetailUpdateDelete
from .views.views_fbv import task_lists_list, task_list_detail, task_detail, tasks_list
from .views.auth import Register
# from .views.auth import register
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', Register.as_view()),
    # path('register/', register),

    path('task_list/', TaskListListCreate.as_view()),
    path('task_list/<int:pk>/', TaskListDetailUpdateDelete.as_view()),
    path('task_list/<int:pk>/tasks/', TaskListCreate.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDelete.as_view()),

    path('task_list_fbv/', task_lists_list),
    path('task_list_fbv/<int:pk>/', task_list_detail),
    path('task_list_fbv/<int:pk>/tasks/', tasks_list),
    path('tasks_fbv/<int:pk>/', task_detail)
]
