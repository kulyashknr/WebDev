from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    #
    # def check_owner(self, request):
    #     return self.owner == request.user


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    due_on = models.DateField()
    status = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def to_json_short(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_long(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.__str__(),
            'due_on': self.due_on.__str__(),
            'status': self.status,
            'task_list': self.task_list.to_json(),
        }

    def check_owner(self, request):
        return self.owner.id == request.user.id