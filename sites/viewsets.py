from .models import Site
from courses.models import Course
from .serializers import SiteSerializer, SiteDetailSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SiteSerializer
        return SiteDetailSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        courses = data["courses"]
        del data["courses"]

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            site = serializer.save()

            for course in courses:
                course_id = course["id"]
                item = Course.objects.get(pk=course_id)
                site.courses.add(item)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data.copy()
        courses = data["courses"]
        del data["courses"]

        site = self.get_object()
        serializer = self.get_serializer(site, data=data)
        if serializer.is_valid():
            site = serializer.save()

            for course in courses:
                course_id = course["id"]
                item = Course.objects.get(pk=course_id)
                site.courses.add(item)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
