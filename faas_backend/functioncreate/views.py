from rest_framework import viewsets, filters

from .models import FunctionCreate,FunctionFile
from .serializers import FunctionSerializer, FunctionFileSerializer


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = FunctionCreate.objects.all()
    serializer_class = FunctionSerializer


class FunctionFileViewSet(viewsets.ModelViewSet):
    queryset = FunctionFile.objects.all()
    serializer_class = FunctionFileSerializer


