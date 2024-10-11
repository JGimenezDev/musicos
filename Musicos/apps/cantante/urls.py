from django.urls import path
from . import views

app_name = 'app_cantante'

urlpatterns = [
    path('lista-de-cantantes/', views.ListarCantantes.as_view(), name='lista_de_cantantes'),
    path('crear-cantante/', views.CrearCantante.as_view(), name='crear_cantante'),
    path('eliminar-cantante/<pk>/', views.EliminarCantante.as_view(), name='eliminar_cantante'),
    path('editar-cantante/<pk>/', views.EditarCantante.as_view(), name='editar_cantante'),
    path('detalle-cantante/<pk>/', views.DetalleCantante.as_view(), name='detalle_cantante'),
]