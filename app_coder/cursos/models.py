from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    anio = models.IntegerField()
    comision = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=40)
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
 #Create your models here.
