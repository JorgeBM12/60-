from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Evento
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def servicios(request):
    return render(request, 'inicio/servicios.html')

@login_required
def eventos(request):

    eventos = Evento.objects.filter(estado='proximo')

    return render(request, 'inicio/eventos.html', {
        'eventos': eventos
    })

def registro(request):
    return render(request, 'inicio/registro_evento.html')

def redirect_user(request):

    if request.user.is_staff:
        return redirect('inicio')

    else:
        return redirect('eventos')

@permission_required('inicio.add_evento')
def crear_evento(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha = request.POST['fecha']
        lugar = request.POST['lugar']
        cupo = request.POST['cupo']
        estado = request.POST['estado']

        Evento.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha=fecha,
            lugar=lugar,
            cupo_maximo=cupo,
            estado=estado
        )

        return redirect('eventos')

    return render(request, 'inicio/crear_evento.html')

@permission_required('inicio.change_evento')
def editar_evento(request, id):

    evento = Evento.objects.get(id=id)

    if request.method == 'POST':

        evento.nombre = request.POST['nombre']
        evento.descripcion = request.POST['descripcion']
        evento.fecha = request.POST['fecha']
        evento.lugar = request.POST['lugar']
        evento.cupo_maximo = request.POST['cupo']
        evento.estado = request.POST['estado']

        evento.save()

        return redirect('eventos')

    return render(request, 'inicio/editar_evento.html', {'evento': evento})

@permission_required('inicio.delete_evento')
def eliminar_evento(request, id):

    evento = Evento.objects.get(id=id)

    evento.delete()

    return redirect('eventos')

def acceso_requerido(request):

    messages.warning(request, "Necesitas iniciar sesión para acceder")

    return redirect('login')

def detalle_evento(request, id):

    evento = Evento.objects.get(id=id)

    return render(request,"inicio/detalle_evento.html",{
        "evento":evento
    })