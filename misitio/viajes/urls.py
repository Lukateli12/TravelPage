from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Propuestas de viaje', views.libros, name='Propuestas de viaje'),
    path('paginas/formulario', views.comprar, name='formulario'),
    ]