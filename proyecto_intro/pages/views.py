from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ChecklistItem
from .forms import CustomUserCreationForm
# Create your views here.
#Las funciones view reciben una request (pedido) y dan una  response (respuesta)
#Ej (renderiza html, el html lo encuentran en la carpeta templates):

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'algo.html')

def info(request):
    # Crear un diccionario de contexto con las variables y valores deseados
    context = {
        'titulo': '¿Cómo podemos reciclar?',
        'imagen1': "https://img.freepik.com/vector-gratis/conjunto-verde-carteles-reciclados_78370-662.jpg?size=626&ext=jpg&ga=GA1.1.867424154.1698105600&semt=sph",
        "manera1": "1. Usa botellas/vasos reutilizables para tus bebidas fuera de casa.",
        "manera2" : "2. Usa bolsas de compras reutilizables, y no solo para hacer las compras",
        "manera3" : "3. Evita contenedores y cubiertos de un solo uso.",
        "credito" : "Información extrahída de The Nature Conservancy. URL: https://www.nature.org/es-us/que-hacemos/nuestras-prioridades/ciudades-saludables/como-reducir-la-basura/",
        "mp1": "Probablemente, ya tienes una botella reutilizable, pero ¿la usas todo el tiempo? Pon esa botella reutilizable en circulación: ahorrarás dinero y reducirás la basura. Además, si llevas tu propia agua cuando sales de tu casa, comprarás menos bebidas más caras por la calle. Esto eliminará los contenedores de uso único en los que vienen. Si bien la mayoría de las latas y botellas pueden reciclarse, se necesita un montón de energía para producirlas, transportarlas a la planta embotelladora y luego a las tiendas.",
        "mp2" : "Al igual que las botellas reutilizables, seguramente tienes una bolsa de compras reutilizable, pero con frecuencia queda olvidada en casa. ¿Y si escribes bolsas arriba de todo de tu lista de compras como recordatorio? También puedes tenerlas siempre en el asiento trasero, así no se te olvidan. Muchas tiendas te harán un reembolso de 5 centavos por cada bolsa, así que, además de reducir tu consumo de bolsas de plástico de un solo uso, también ahorrarás unos centavos.",
        "mp3" : "Siempre que sea posible, intenta no usar vasos de café, cubiertos, pajillas y servilletas descartables. Algunos negocios incluso te darán un descuento sobre tu café si llevas tu propia taza. En la oficina, ten un juego de vajilla, cubiertos, bol y taza quepuedas lavar y volver a usar. Evita completamente las pajillas o compra las reutilizables de metal. Recuerda: muchos de estos artículos están hechos de plástico, fueron transportados en un camión y terminarán en un vertedero una vez que los usamos solo una vez. Todo lo que podamos hacer para reducir nuestro consumo de estos productos contribuye a lograr un gran impacto. ",
        "imagen2" : "https://aseca.com/wp-content/uploads/2020/06/Todo-reciclaje.png"
    }
    return render(request, 'manerasdereciclar.html', context)

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

