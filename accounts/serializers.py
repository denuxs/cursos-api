from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "is_active"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = {}
        data["user"]["username"] = self.user.username
        data["user"]["email"] = self.user.email
        data["user"]["firstname"] = self.user.first_name
        data["user"]["lastname"] = self.user.last_name
        data["user"]["is_superuser"] = self.user.is_superuser
        data["user"]["id"] = self.user.id

        return data

class MyTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = {}
        data["user"]["username"] = self.user.username
        data["user"]["email"] = self.user.email
        data["user"]["firstname"] = self.user.first_name
        data["user"]["lastname"] = self.user.last_name
        data["user"]["id"] = self.user.id

        return data