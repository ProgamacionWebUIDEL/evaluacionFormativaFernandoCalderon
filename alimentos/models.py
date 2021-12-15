from django.db import models

# Create your models here.
class Alimento(models.Model):
    nomAlimento = models.CharField(max_length=100, help_text='nombre de los alimentos')
    tipoAlimento = models.CharField(max_length=100, help_text='tipo de alimentos')
    numCalorias = models.IntegerField(help_text='numero de calorias por porcion')

class Mascota(models.Model):
    nomMascota = models.CharField(max_length=100, help_text='nombre de la mascota')
    razaMascota = models.CharField(max_length=100, help_text='raza de la mascota')
    edadMascota = models.IntegerField(help_text='edad de la mascota')
    pesoMascota = models.CharField(max_length=100, help_text='peso de la mascota que')