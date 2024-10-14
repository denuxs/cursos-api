from .models import Evaluation
from .serializers import EvaluationSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
