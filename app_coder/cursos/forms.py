from django import forms

from .models import Curso, Estudiante, Profesor,Avatar

from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User


class CursoForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    comision = forms.CharField(max_length=40, required=False)
    anio = forms.IntegerField(required=False)
    fecha_inicio = forms.DateField(required=False)
    fecha_fin = forms.DateField(required=False)
    
    class Meta:
        model = Curso
        fields = ['curso', 'comision', 'anio', 'fecha_inicio', 'fecha_fin']
    
    
class ProfesorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=40, required=False)
    apellido = forms.CharField(max_length=40, required=False)
    email = forms.EmailField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    especialidad = forms.CharField(max_length=40, required=False)
    
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'especialidad']

    
    
class EstudianteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=40, required=False)
    apellido = forms.CharField(max_length=40, required=False)
    email = forms.EmailField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']
        
        

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True,label='Email')
    first_name = forms.CharField( required=True, label='Nombre')  
    last_name = forms.CharField( required=True, label='Apellido')
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
        