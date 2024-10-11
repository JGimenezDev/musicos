from django.urls import path
from . import views

app_name = 'app_artista'

urlpatterns = [
    path('lista-de-artistas/', views.ListarArtistas.as_view(), name='lista_de_artistas'),
    path('crear-artista/', views.CrearArtista.as_view(), name='crear_artista'),
    path('eliminar-artista/<pk>/', views.EliminarArtista.as_view(), name='eliminar_artista'),
    path('editar-artista/<pk>/', views.EditarArtista.as_view(), name='editar_artista'),
    path('detalle-artista/<pk>/', views.DetalleArtista.as_view(), name='detalle_artista'),
]