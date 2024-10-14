from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
