from django import template
from django.contrib.auth.decorators import login_required
register = template.Library()

@register.filter(name='getfecha')
def getfecha(fila, fecha):
    return fila.get(fecha, '') == 'X'