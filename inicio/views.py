from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Evento, Inscripcion
from django.contrib.auth.decorators import login_required, permission_required


def inicio(request):
    eventos = Evento.objects.filter(estado='proximo')[:3]

    return render(request, 'inicio/inicio.html',{
        'eventos':eventos
    })


@login_required
def servicios(request):
    return render(request, 'inicio/servicios.html')


@login_required
def eventos(request):

    eventos = Evento.objects.filter(estado='proximo')

    # contar inscritos por evento
    for evento in eventos:
        evento.inscritos = Inscripcion.objects.filter(evento=evento).count()

    return render(request, 'inicio/eventos.html', {
        'eventos': eventos
    })


def registro(request):
    return render(request, 'inicio/registro_evento.html')


@login_required
def redirect_user(request):

    if request.user.is_staff:
        return redirect('inicio') 
    else:
        return redirect('eventos')


@permission_required('inicio.add_evento')
def crear_evento(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        lugar = request.POST.get('lugar')
        cupo = request.POST.get('cupo')
        estado = request.POST.get('estado')

        # VALIDACIÓN
        if not nombre or not fecha or not cupo:
            messages.error(request, "Campos obligatorios faltantes")
            return redirect('crear_evento')

        Evento.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha=fecha,
            lugar=lugar,
            cupo_maximo=cupo,
            estado=estado
        )

        messages.success(request, "Evento creado correctamente")
        return redirect('eventos')

    return render(request, 'inicio/crear_evento.html')


@permission_required('inicio.change_evento')
def editar_evento(request, id):

    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':

        evento.nombre = request.POST.get('nombre')
        evento.descripcion = request.POST.get('descripcion')
        evento.fecha = request.POST.get('fecha')
        evento.lugar = request.POST.get('lugar')
        evento.cupo_maximo = request.POST.get('cupo')
        evento.estado = request.POST.get('estado')

        evento.save()

        messages.success(request, "Evento actualizado")
        return redirect('eventos')

    return render(request, 'inicio/editar_evento.html', {'evento': evento})


@permission_required('inicio.delete_evento')
def eliminar_evento(request, id):

    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado")
        return redirect('eventos')

    return render(request, 'inicio/confirmar_eliminar.html', {'evento': evento})


def acceso_requerido(request):
    messages.warning(request, "Necesitas iniciar sesión para acceder")
    return redirect('login')


# PROTEGIDO
@login_required
def detalle_evento(request, id):

    evento = get_object_or_404(Evento, id=id)
    inscritos = Inscripcion.objects.filter(evento=evento)
    total_inscritos = inscritos.count()

    porcentaje = 0
    if evento.cupo_maximo > 0:
        porcentaje = (total_inscritos / evento.cupo_maximo) * 100

    return render(request, "inicio/detalle_evento.html", {
        "evento": evento,
        "inscritos": inscritos,
        "total_inscritos": total_inscritos,
        "porcentaje": porcentaje,
        "cupo_disponible": total_inscritos < evento.cupo_maximo
    })


def inscribirse(request, id):

    evento = get_object_or_404(Evento, id=id)

    # CONTROL DE CUPO
    inscritos = Inscripcion.objects.filter(evento=evento).count()

    if inscritos >= evento.cupo_maximo:
        messages.error(request, "El evento ya está lleno")
        return redirect('eventos')

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')

        # VALIDACIÓN
        if not nombre or not correo:
            messages.error(request, "Faltan campos obligatorios")
            return redirect('inscribirse', id=id)

        Inscripcion.objects.create(
            nombre=nombre,
            edad=request.POST.get('edad'),
            correo=correo,
            telefono=request.POST.get('telefono'),
            ciudad=request.POST.get('ciudad'),
            estado=request.POST.get('estado'),
            evento=evento
        )

        messages.success(request, "Inscripción exitosa")
        return redirect('eventos')

    return render(request, 'inicio/inscripcion.html', {'evento': evento})