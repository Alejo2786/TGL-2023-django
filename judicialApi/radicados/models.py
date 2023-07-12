from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Proceso(models.Model):
    numero_expediente = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    juez_encargado = models.ForeignKey(User, on_delete=models.CASCADE)
    juez_encargado = models.CharField(max_length=100)
    participantes = models.ManyToManyField('Participante', related_name='procesos_participantes')

class DocumentoProceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='documentos_procesos/')

class ComentarioProceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Participante(models.Model):
    nombre = models.CharField(max_length=100)