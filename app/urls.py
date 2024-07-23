from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('editar/<int:id>/', views.editar_articulo, name='editar_articulo'),
    path('eliminar/<int:id>/', views.eliminar_articulo, name='eliminar_articulo'),
]