from django.db import models
from .managers import CantanteManager


class Cantante(models.Model):
    
    nombre = models.CharField(max_length=50, blank=False, null=False)
    
    objects = CantanteManager()
    
    def __str__(self):
        return f'{self.nombre}'