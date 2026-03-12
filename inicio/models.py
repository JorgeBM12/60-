from django.db import models

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
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre