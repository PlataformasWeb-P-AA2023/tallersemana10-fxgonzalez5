from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField('Nombre del Equipo' ,max_length=30, unique=True)
    siglas = models.CharField(max_length=5)
    username = models.CharField('Username de Twitter', max_length=30)
    campeonatos = models.ManyToManyField('Campeonato', through='Participacion')

    def __str__(self):
        return "Equipo: %s - %s - %s" % (self.nombre, self.siglas, self.username)
    

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    nro_camiseta = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return "Jugador: %s - %s - %d - %d" % (self.nombre, self.posicion, self.nro_camiseta, self.sueldo)
    

class Campeonato(models.Model):
    nombre = models.CharField('Nombre del Camponato' ,max_length=30)
    auspiciante = models.CharField('Nombre del Auspiciante', max_length=30)
    equipos = models.ManyToManyField(Equipo, through='Participacion')

    def __str__(self):
        return "Campeonato: %s - %s" % (self.nombre, self.auspiciante)
    

class Participacion(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(Equipo, related_name='lasparticipaciones', on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='lasparticipaciones', on_delete=models.CASCADE)

    def __str__(self):
        return "Participación: %d - %s - %s" % \
                (self.anio, self.equipo, self.campeonato)