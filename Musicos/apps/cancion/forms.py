from django import forms
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = [
            'titulo',
            'artista',
            'cantantes',
            'tono_original',
            'tono_cantante'
        ]