from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    Telefono=models.CharField(max_length=9)

    def __str__(self):
        return self.nombre, self.direccion, self.email, self.Telefono

class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    colores = models.CharField(verbose_name="Colores", max_length=50)
    precio = models.IntegerField(verbose_name="Precio")
    tamaño = models.IntegerField(verbose_name="Tamaño")
    descripcion = models.CharField(verbose_name="Descripcion", max_length=100)

    def __str__(self):
        return self.nombre


class Galeria(models.Model):
    nombre_imagen = models.CharField(verbose_name="Nombre Imagen", max_length=50)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=100)