from .models import Course, Video
from .serializers import CourseSerializer, CourseDetailSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CourseSerializer
        return CourseDetailSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        videos = data.pop("videos")

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            course = serializer.save()

            for video in videos:
                item = {}
                item["title"] = video["title"]
                item["description"] = video["description"]
                item["url"] = video["url"]
                item["duration"] = video["duration"]
                item["course"] = course

                Video.objects.create(**item)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data.copy()
        videos = data.pop("videos")

        course = self.get_object()
        serializer = self.get_serializer(course, data=data)
        if serializer.is_valid():
            course = serializer.save()

            for video in videos:
                video_id = video["id"]
                
                item = {}
                item["title"] = video["title"]
                item["description"] = video["description"]
                item["url"] = video["url"]
                item["duration"] = video["duration"]
                item["course"] = course

                if video_id:
                    v = Video.objects.get(pk=video_id)

                    v.title = item["title"]
                    v.description = item["description"]
                    v.duration = item["duration"]
                    v.url = item["url"]
                    v.save()
                else:
                    Video.objects.create(**item)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
