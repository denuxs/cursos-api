from django.contrib import admin

from .models import Country, Department

admin.site.register(Country)
admin.site.register(Department)