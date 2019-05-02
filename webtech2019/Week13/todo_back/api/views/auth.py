from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from ..serializers import UserModelSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView


class Register(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        return serializer.save()
