from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ChecklistItem
from .forms import CustomUserCreationForm
# Create your views here.
#Las funciones view reciben una request (pedido) y dan una  response (respuesta)
#Ej (renderiza html, el html lo encuentran en la carpeta templates):

def home(request):
    return render(request, 'base.html')

def decir_hola(request):
    return render(request, 'algo.html')

#en vez de dejar el login_required como comentario, creense un superusuario
#el comando es 'python manage.py createsuperuser'
#que si me dejan la wea comentada no voy a saberlo
@login_required
def reciclaje(request):
    elementos = ChecklistItem.objects.all()
    print(elementos)
    return render(request, 'herramienta1.html', {'elementos': elementos})

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user= authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')


    return render(request, 'registration/register.html', data)
