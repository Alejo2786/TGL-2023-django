

from rest_framework import serializers
from .models import Proceso, DocumentoProceso, ComentarioProceso

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = '__all__'

class DocumentoProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoProceso
        fields = '__all__'

class ComentarioProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioProceso
        fields = '__all__'

