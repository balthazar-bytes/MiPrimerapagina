from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
        label='Contenido'
        )
    
    class Meta:
        model = Mensaje
        field = ['contenido']
        