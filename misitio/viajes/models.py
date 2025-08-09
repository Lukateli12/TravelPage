from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)