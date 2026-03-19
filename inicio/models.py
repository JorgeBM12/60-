from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    beneficios = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)

    cupo_maximo = models.IntegerField()

    estado = models.CharField(
        max_length=20,
        choices=[
            ('proximo','Próximo'),
            ('realizado','Realizado')
        ]
    )

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class RegistroEvento(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)