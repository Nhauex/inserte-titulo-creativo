from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ChecklistItem,UserProfile
from .forms import CustomUserCreationForm
from .models import News,Category,Comment
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
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
        "mp3" : "Siempre que sea posible, intenta no usar vasos de café, cubiertos, pajillas y servilletas descartables. Algunos negocios incluso te darán un descuento sobre tu café si llevas tu propia taza. En la oficina, ten un juego de vajilla, cubiertos, bol y taza que puedas lavar y volver a usar. Evita completamente las pajillas o compra las reutilizables de metal. Recuerda: muchos de estos artículos están hechos de plástico, fueron transportados en un camión y terminarán en un vertedero una vez que los usamos solo una vez. Todo lo que podamos hacer para reducir nuestro consumo de estos productos contribuye a lograr un gran impacto. ",
        "imagen2" : "https://aseca.com/wp-content/uploads/2020/06/Todo-reciclaje.png"
    }
    return render(request, 'manerasdereciclar.html', context)

#en vez de dejar el login_required como comentario, creense un superusuario
#el comando es 'python manage.py createsuperuser'
#que si me dejan las cosas comentadas no voy a saberlo
@login_required
def reciclaje(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        selected_items = request.POST.getlist('item')  # Get selected items from checkboxes
        current_date = datetime.now().date()
        

        for item_name in selected_items:
            #esto es WIP para el cooldown
            existing_item = ChecklistItem.objects.filter(user=request.user.username, elementos=item_name, fecha=current_date).first



            item = ChecklistItem.objects.create(user= request.user.username, elementos=item_name, fecha=current_date)
            user_profile.checklist_items.add(item)
            user_profile.puntos += 1
            user_profile.save()

        return HttpResponse('Reciclaje Registrado Correctamente y Puntos añadidos, vuelve mañana! <a href="/">Volver al inicio</a>')
    
    return render(request, 'herramienta1.html', {'user_profile': user_profile})

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

def xd(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:4]
    three_categories=Category.objects.all()[0:3]
    return render(request,'xd.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

# All News
def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted but in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    })

def profile(request):
    user=request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)  # Obtener el perfil del usuario actual
    checklistitem = user_profile.checklist_items.all()
    return render(request, 'profile.html', {'user_profile': user_profile, 'checklistitem': checklistitem})

def mark_news_as_read(request, news_title):
    # Obtener el usuario actual
    user = request.user

    # Obtener el perfil del usuario actual
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    # Agregar la noticia leída al UserProfile si aún no está presente
    user_profile.add_read_news_title(news_title)

    return redirect(request.META.get('HTTP_REFERER'))