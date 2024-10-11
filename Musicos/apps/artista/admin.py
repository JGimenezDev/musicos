from django.contrib import admin
from .models import Artista


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']