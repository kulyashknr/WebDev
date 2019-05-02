from django.shortcuts import render
from .models import TaskList, Task
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import TaskListSerializer, TaskModelSerializer
from django.http import Http404


class TaskListListCreate(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.all()

    def perform_create(self, serializer):
        return serializer.save()


class TaskListDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer
    lookup_field = 'pk'

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskModelSerializer
    lookup_field = 'pk'

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Task.objects.filter(task_list=self.get_object())

    def perform_create(self, serializer):
        return serializer.save(task_list=self.get_object())


class TaskDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskModelSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Task.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()