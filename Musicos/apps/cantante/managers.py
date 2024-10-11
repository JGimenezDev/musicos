from django.db import models
from django.db.models import Q


class CantanteManager(models.Manager):
    def buscar_cantantes(self, cant):
        res = self.filter(
            nombre__icontains = cant
        )
        return res