from ..models import TaskList, Task
from rest_framework import generics
from ..serializers import TaskListSerializer, TaskModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class TaskListListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TaskListDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = TaskListSerializer
    lookup_field = 'pk'

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class TaskListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = TaskModelSerializer
    lookup_field = 'pk'

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Task.objects.filter(task_list=self.get_object())

    def perform_create(self, serializer):
        return serializer.save(task_list=self.get_object(), owner=self.request.user)


class TaskDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = TaskModelSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Task.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()