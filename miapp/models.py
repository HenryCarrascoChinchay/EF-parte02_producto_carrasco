from django.db import models

# Create your models here.
class Docente(models.Model):
    codigo = models.CharField(max_length=150)
    nombre = models.TextField()
    apellido_paterno = models.TextField()
    apellido_materno = models.TextField()
    dni = models.CharField(max_length=8)
    publicado = models.BooleanField()
    # auto_now_add me permitirá registrar
    # la fecha cuando cree el registro
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateTimeField(auto_now=True)
    estado = models.TextField()
    