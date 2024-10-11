from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cantante
from .forms import CantanteForm


class ListarCantantes(ListView):
    model = Cantante
    template_name = "cantante/lista_cantantes.html"
    context_object_name = 'cantantes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cantante = self.request.GET.get('cant', '')
        if cantante != '':
            return Cantante.objects.buscar_cantantes(cantante)
        return queryset
    

class CrearCantante(CreateView):
    form_class = CantanteForm
    template_name = "cantante/crear_cantante.html"
    success_url = reverse_lazy('app_cantante:lista_de_cantantes')
    

class EliminarCantante(DeleteView):
    model = Cantante
    template_name = "cantante/eliminar_cantante.html"
    context_object_name = 'cantante'
    success_url = reverse_lazy('app_cantante:lista_de_cantantes')


class EditarCantante(UpdateView):
    model = Cantante
    form_class = CantanteForm
    template_name = "cantante/editar_cantante.html"
    context_object_name = 'cantante'
    
    def get_success_url(self):
        return reverse('app_cantante:detalle_cantante', kwargs={'pk': self.object.pk})
    

class DetalleCantante(DetailView):
    model = Cantante
    template_name = "cantante/detalle_cantante.html"
    context_object_name = 'cantante'

