from django.urls import path
from . import views
#Configuracion de url, para mapear la funcion decirhola a la url testeo/hola
urlpatterns = [
    path('', views.decir_hola),
    path('paginareciclaje.html', views.reciclaje)
]