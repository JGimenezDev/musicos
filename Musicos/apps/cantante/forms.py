from django import forms
from .models import Cantante


class CantanteForm(forms.ModelForm):
    class Meta:
        model = Cantante
        fields = ['nombre']