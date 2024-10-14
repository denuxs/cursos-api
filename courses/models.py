from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]

class Video(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=140)
    duration = models.CharField(max_length=140)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="videos"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]