from django.contrib.auth.models import User
from .models import Student

from rest_framework import serializers
from rest_framework.parsers import FileUploadParser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_active", 'is_superuser']


class StudentSerializer(serializers.ModelSerializer):
    # parser_class = (FileUploadParser,)
    class Meta:
        model = Student
        fields = "__all__"


class StudentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = "__all__"
