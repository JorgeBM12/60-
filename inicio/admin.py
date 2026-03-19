from django.contrib import admin
from .models import Servicio,Evento,Inscripcion

# Register your models here.
# Inline (este inline es opcional para que aparezcan las inscripciones directamente)
class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 0

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'cupo_maximo', 'total_inscritos')
    inlines = [InscripcionInline]

    def total_inscritos(self, obj):
        return Inscripcion.objects.filter(evento=obj).count()


# Registros
admin.site.register(Servicio)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Inscripcion)