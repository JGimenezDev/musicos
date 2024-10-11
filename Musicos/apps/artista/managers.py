from django.db import models
from django.db.models import Q


class ArtistaManager(models.Manager):
    def buscar_artistas(self, art):
        res = self.filter(
            nombre__icontains = art
        )
        return res