from rest_framework import serializers
from .models import TaskList, Task
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.get("password")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return user

    class Meta:
        model = User
        fields = '__all__'


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    owner = UserModelSerializer

    def create(self, validated_data):
        return TaskList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer
    owner = UserModelSerializer

    class Meta:
        model = Task
        fields = '__all__'
