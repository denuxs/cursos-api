from django.contrib.auth.models import User

from .models import Student
from .serializers import StudentSerializer, UserSerializer, StudentDetailSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=140)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=['post'])
    def password(self, request, pk=None):
        data = request.data.copy()
        password = data['password']

        user = self.get_object()

        serializer = PasswordSerializer(data=data)
        if serializer.is_valid():
            user.set_password(password)
            user.save()

            serializer = UserSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return StudentSerializer
        return StudentDetailSerializer
