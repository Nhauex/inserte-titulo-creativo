from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Las funciones view reciben una request (pedido) y dan una  response (respuesta)
#Ej (renderiza html, el html lo encuentran en la carpeta templates):
def decir_hola(roq):
    return render(roq, 'algo.html')

#Podemos asignarle una Url a esta view -> vease urls.py