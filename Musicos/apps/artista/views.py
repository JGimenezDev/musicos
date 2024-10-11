from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Artista
from .forms import ArtistaForm



class ListarArtistas(ListView):
    model = Artista
    template_name = "artista/lista_artistas.html"
    context_object_name = 'artistas'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        artista = self.request.GET.get('art', '')
        if artista != '':
            return Artista.objects.buscar_artistas(artista)
        return queryset


class CrearArtista(CreateView):
    form_class = ArtistaForm
    template_name = "artista/crear_artista.html"
    success_url = reverse_lazy('app_artista:lista_de_artistas')


class EliminarArtista(DeleteView):
    model = Artista
    template_name = "artista/eliminar_artista.html"
    context_object_name = 'artista'
    success_url = reverse_lazy('app_artista:lista_de_artistas')


class EditarArtista(UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "artista/editar_artista.html"
    context_object_name = 'artista'
    
    def get_success_url(self):
        return reverse('app_artista:detalle_artista', kwargs={'pk': self.object.pk})


class DetalleArtista(DetailView):
    model = Artista
    template_name = "artista/detalle_artista.html"
    context_object_name = 'artista'
