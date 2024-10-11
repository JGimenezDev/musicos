from django.db import models
from apps.cantante.models import Cantante
from apps.artista.models import Artista
from .managers import CancionManager


class Tonalidad(models.Model):
    
    tono = models.CharField(max_length=5, blank=False, null=False)
    
    def __str__(self):
        return f'{self.tono}'
    

class Cancion(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)
    artista = models.ForeignKey(Artista,
                                on_delete=models.CASCADE,
                                related_name = 'artista_cancion',
                                blank=True, null = True)
    cantantes = models.ManyToManyField(Cantante, blank=True, null=True)
    tono_original = models.CharField(max_length=5, blank=True, null=True)
    tono_cantante = models.CharField(max_length=5, blank=True, null=True)
    
    objects = CancionManager()
    
    class Meta:
        unique_together = [["titulo", "artista"]]
        
    def __str__(self):
        return f'{self.titulo}'