from django.shortcuts import render

from rest_framework import viewsets
from .models import Proceso, DocumentoProceso, ComentarioProceso
from .serializers import ProcesoSerializer, DocumentoProcesoSerializer, ComentarioProcesoSerializer

class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer

class DocumentoProcesoViewSet(viewsets.ModelViewSet):
    queryset = DocumentoProceso.objects.all()
    serializer_class = DocumentoProcesoSerializer

class ComentarioProcesoViewSet(viewsets.ModelViewSet):
    queryset = ComentarioProceso.objects.all()
    serializer_class = ComentarioProcesoSerializer

