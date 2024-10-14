from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from students.models import Student
from rest_framework import permissions
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=140, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length=140)
    email = serializers.EmailField(max_length=140, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=140)
    last_name = serializers.CharField(max_length=140)
    is_active = serializers.BooleanField(default=True)

class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        user = request.data.copy()

        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            user = User.objects.create_user(
                user["username"],
                user["email"],
                user["password"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                is_active=False
            )

            Student.objects.create(user=user)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
