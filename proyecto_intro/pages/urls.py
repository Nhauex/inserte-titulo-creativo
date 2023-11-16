from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
#Configuracion de url, para mapear la funcion decirhola a la url testeo/hola
urlpatterns = [
    path('herramienta1/', views.reciclaje, name='herramienta1'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    path('info/', views.info, name='info'),
    path('xd/',views.xd,name='xd'),
    path('all-news/',views.all_news,name='all-news'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('profile/',views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    