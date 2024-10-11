from django.db import models
from .managers import ArtistaManager


class Artista(models.Model):
    
    nombre = models.CharField(max_length=50, blank=False, null=False)
    
    objects = ArtistaManager()
    
    def __str__(self):
        return f'{self.nombre}'
    
