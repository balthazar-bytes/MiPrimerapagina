from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        return f"De: {self.emisor.username} | Para: {self.receptor.username} | {self.timestamp.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        ordering = ['timestamp']
        
        
        