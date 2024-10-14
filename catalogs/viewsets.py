from .models import Catalog
from .serializers import CatalogSerializer

from rest_framework import viewsets


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
