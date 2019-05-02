from rest_framework.decorators import api_view
from ..models import Task, TaskList
from ..serializers import TaskListSerializer, TaskModelSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def task_lists_list(request, format=None):
    if request.method == 'GET':
        lists = TaskList.objects.all()
        serializer = TaskListSerializer(lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_list_detail(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT' or 'PATCH':
        serializer = TaskListSerializer(instance=list , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tasks_list(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tasks = Task.objects.filter(task_list=list)
        serializer = TaskModelSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskModelSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT' or 'POST':
        serializer = TaskModelSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)