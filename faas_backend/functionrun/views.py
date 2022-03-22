from rest_framework import viewsets, filters

from .models import RunPath
from .serializers import RunPathSerializer


class RunPathViewSet(viewsets.ModelViewSet):
    queryset = RunPath.objects.all()
    serializer_class = RunPathSerializer

