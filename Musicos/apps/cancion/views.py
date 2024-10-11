from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cancion
from .forms import CancionForm


class ListarCanciones(ListView):
    model = Cancion
    template_name = "cancion/lista_canciones.html"
    context_object_name = 'canciones'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cancion = self.request.GET.get('cancion', '')
        if cancion != '':
            return Cancion.objects.buscar_canciones(cancion)
        return queryset
    

class DetalleCancion(DetailView):
    model = Cancion
    template_name = "cancion/detalle_cancion.html"
    context_object_name= 'cancion'
    
    
class EditarCancion(UpdateView):
    model = Cancion
    form_class = CancionForm
    template_name = "cancion/editar_cancion.html"
    context_object_name = 'cancion'
    
    
    def get_success_url(self):
        return reverse('app_cancion:detalle_cancion', kwargs={'pk': self.object.pk})


class EliminarCancion(DeleteView):
    model = Cancion
    template_name = "cancion/eliminar_cancion.html"
    context_object_name = 'cancion'
    success_url = reverse_lazy('app_cancion:lista_de_canciones')


class CrearCancion(CreateView):
    model = Cancion
    form_class = CancionForm
    template_name = "cancion/crear_cancion.html"
    
    def get_success_url(self):
        return reverse('app_cancion:detalle_cancion', kwargs={'pk': self.object.pk})
