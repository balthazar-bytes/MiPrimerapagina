from django import forms
from .models import Mensaje 
class MensajeForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3, 
            'class': 'form-control', 
            'placeholder': 'Escribe tu mensaje aquí...'
        }),
        label="" 
    )

    class Meta:
        model = Mensaje
        fields = ['contenido'] 