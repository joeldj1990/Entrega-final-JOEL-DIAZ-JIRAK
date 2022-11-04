from django.db import models

# Create your models here.

class Armazones(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    tamagno = models.CharField(max_length=30)
    precio = models.IntegerField()
    codigo = models.IntegerField()


class Cristales(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    graduacion = models.IntegerField()
    precio = models.IntegerField()
    codigo = models.IntegerField()


class Lentes_Sol(models.Model):
    marca = models.CharField(max_length=30)
    color_armazon = models.CharField(max_length=30)
    color_lente = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    tamagno = models.CharField(max_length=30)
    precio = models.IntegerField()
    codigo = models.IntegerField()
