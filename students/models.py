from django.db import models

from locations.models import Department, Country
from catalogs.models import Catalog
from django.contrib.auth.models import User
from sites.models import Site

# from django.contrib.auth import get_user_model
# User = get_user_model()

DNI_TYPE = [
    ("dni", "Cedula"),
    ("passport", "Pasaporte"),
]


class Student(models.Model):
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to="avatar", default="default.jpg", blank=True, null=True
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    identification_type = models.CharField(max_length=140, choices=DNI_TYPE, null=True)
    identification = models.CharField(max_length=140, null=True)
    company = models.CharField(max_length=140, null=True)
    # deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-id"]
