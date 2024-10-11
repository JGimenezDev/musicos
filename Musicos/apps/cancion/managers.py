from django.db import models
from django.db.models import Q


class CancionManager(models.Manager):
    def buscar_canciones(self, cancion):
        res = self.filter(
            titulo__icontains = cancion
        )
        return res