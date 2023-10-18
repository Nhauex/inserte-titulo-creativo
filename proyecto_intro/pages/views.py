from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#Las funciones view reciben una request (pedido) y dan una  response (respuesta)
#Ej (renderiza html, el html lo encuentran en la carpeta templates):
def decir_hola(req):
    return render(req, 'algo.html')

#Podemos asignarle una Url a esta view -> vease urls.py
@login_required
def reciclaje(req):
    return render(req, 'herramienta1.html' )

def login(req):
    return render(req, 'login.html')

def exit(req):
    logout(req)
    return redirect('home')