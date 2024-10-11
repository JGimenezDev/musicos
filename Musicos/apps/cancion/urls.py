from django.urls import path
from . import views

app_name = 'app_cancion'

urlpatterns = [
    path('lista-de-canciones/', views.ListarCanciones.as_view(), name='lista_de_canciones'),
    path('detalle-de-cancion/<pk>/', views.DetalleCancion.as_view(), name='detalle_cancion'),
    path('editar-cancion/<pk>/', views.EditarCancion.as_view(), name='editar_cancion'),
    path('eliminar-cancion/<pk>/', views.EliminarCancion.as_view(), name='eliminar_cancion'),
    path('crear-cancion/', views.CrearCancion.as_view(), name='crear_cancion'),
]