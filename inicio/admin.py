from django.contrib import admin
from .models import Servicio,Evento,Inscripcion

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Evento)
admin.site.register(Inscripcion)