from django.shortcuts import render
from .models import Evento

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

def eventos(request):

    eventos = Evento.objects.filter(estado='proximo')

    return render(request, 'inicio/eventos.html', {
        'eventos': eventos
    })

def registro(request):
    return render(request, 'inicio/registro_evento.html')