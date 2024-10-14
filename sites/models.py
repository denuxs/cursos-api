from django.db import models

from locations.models import Department, Country
from catalogs.models import Catalog
from courses.models import Course


class Site(models.Model):
    name = models.CharField(max_length=140)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    courses = models.ManyToManyField(Course, blank=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
