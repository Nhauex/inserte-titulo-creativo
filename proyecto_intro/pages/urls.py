from django.urls import path
from . import views
#Configuracion de url, para mapear la funcion decirhola a la url testeo/hola
urlpatterns = [
    path('herramienta1/', views.reciclaje, name='herramienta1'),
    path('login/', views.login, name='login'),
    path('logout/', views.exit, name='exit'),
]

    