from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import ChecklistItem
# Create your views here.
#Las funciones view reciben una request (pedido) y dan una  response (respuesta)
#Ej (renderiza html, el html lo encuentran en la carpeta templates):

def home(request):
    return render(request, 'base.html')

def decir_hola(req):
    return render(req, 'algo.html')

#en vez de dejar el login_required como comentario, creense un superusuario
#el comando es 'python manage.py createsuperuser'
#que si me dejan la wea comentada no voy a saberlo
@login_required
def reciclaje(req):
    elementos = ChecklistItem.objects.all()
    print(elementos)
    return render(req, 'herramienta1.html', {'elementos': elementos})

def exit(req):
    logout(req)
    return redirect('home')

