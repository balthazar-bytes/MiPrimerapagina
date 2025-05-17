from django import forms

from .models import Curso, Estudiante, Profesor

class CursoForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    comision = forms.CharField(max_length=40, required=False)
    anio = forms.IntegerField(required=False)
    fecha_inicio = forms.DateField(required=False)
    fecha_fin = forms.DateField(required=False)
    
    
class ProfesorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=40, required=False)
    apellido = forms.CharField(max_length=40, required=False)
    email = forms.EmailField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    especialidad = forms.CharField(max_length=40, required=False)
    '''class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    '''
    
    
class EstudianteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=40, required=False)
    apellido = forms.CharField(max_length=40, required=False)
    email = forms.EmailField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    