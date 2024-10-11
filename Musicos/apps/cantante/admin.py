from django.contrib import admin
from .models import Cantante


@admin.register(Cantante)
class CantanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']