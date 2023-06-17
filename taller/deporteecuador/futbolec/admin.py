from django.contrib import admin
from futbolec.models import Equipo, Jugador, Campeonato, Participacion

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username')
    search_fields = ('nombre', 'siglas')

admin.site.register(Equipo, EquipoAdmin)


class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'nro_camiseta', 'sueldo', 'get_equipo')
    raw_id_fields = ('equipo',)

    def get_equipo(self, obj):
        return obj.equipo.nombre
    
admin.site.register(Jugador, JugadorAdmin)


class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'auspiciante')
    search_fields = ('nombre', 'auspiciante')

admin.site.register(Campeonato, CampeonatoAdmin)


class ParticipacionAdmin(admin.ModelAdmin):
    list_display = ('anio', 'get_equipo', 'get_campeonato')
    search_fields = ('anio', 'equipo__nombre', 'campeonato__nombre')
    raw_id_fields = ('equipo', 'campeonato',)

    def get_equipo(self, obj):
        return obj.equipo.nombre
    
    def get_campeonato(self, obj):
        return obj.campeonato.nombre

admin.site.register(Participacion, ParticipacionAdmin)