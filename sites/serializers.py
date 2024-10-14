from rest_framework import serializers

from .models import Site
from locations.serializers import CountrySerializer, DepartmentSerializer


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = "__all__"


class SiteDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Site
        fields = "__all__"
