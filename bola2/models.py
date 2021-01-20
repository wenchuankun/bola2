from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    colores = models.CharField(verbose_name="Colores", max_length=50)
    precio = models.IntegerField(verbose_name="Precio", max_length=50)
    tamaño = models.IntegerField(verbose_name="Tamaño")
    descripcion = models.CharField(verbose_name="Descripcion", max_length=50)