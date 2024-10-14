from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Department(models.Model):
    name = models.CharField(max_length=140)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
