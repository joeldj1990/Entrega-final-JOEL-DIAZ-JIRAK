from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Armazones(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    tamagno = models.CharField(max_length=30)
    precio = models.IntegerField()
    codigo = models.IntegerField()
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    medidas = models.CharField(max_length=30, default="-")
    tipo = models.CharField(max_length=30, default="-")
    peso = models.CharField(max_length=30, default="-")
    estilo = models.CharField(max_length=30, default="-")
    fecha = models.DateField(auto_now=False, auto_now_add=False, default="1111-11-11")

    def __str__(self):
        return f'Armazón {self.marca} de {self.material}, color {self.color}, ${self.precio}'


class Cristales(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    graduacion = models.CharField(max_length=30)
    precio = models.IntegerField()
    codigo = models.IntegerField()
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    laboratorio = models.CharField(max_length=30, default="-")
    duracion = models.CharField(max_length=30, default="-")
    prescripcion = models.CharField(max_length=40, default="-")
    fecha = models.DateField(auto_now=False, auto_now_add=False, default="1111-11-11")


    def __str__(self):
        return f'Lentes {self.marca} {self.color}, material {self.material}, ${self.precio}'


class Lentes_Sol(models.Model):
    marca = models.CharField(max_length=30)
    color_armazon = models.CharField(max_length=30)
    color_lente = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    tamagno = models.CharField(max_length=30)
    precio = models.IntegerField()
    codigo = models.IntegerField()
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    medidas = models.CharField(max_length=30, default="-")
    tipo = models.CharField(max_length=30, default="-")
    peso = models.CharField(max_length=30, default="-")
    polarizado = models.CharField(max_length=20, default="-")
    antireflejo = models.CharField(max_length=20, default="-")
    estilo = models.CharField(max_length=30, default="-")
    fecha = models.DateField(auto_now=False, auto_now_add=False, default="1111-11-11")

    def __str__(self):
        return f'Lentes de sol {self.marca} de {self.material}, armazón color {self.color_armazon} y cristales {self.color_lente}, ${self.precio}'


def user_path(instance, filename):
    return 'avatares/{0}/{1}'.format(instance.user.id, filename)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=user_path, default='avatares/default.jpg')



    def __str__(self):
        return f' {self.user} - {self.imagen}'

@ receiver(post_save, sender=User)
def crear_avatar(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.create(user=instance)