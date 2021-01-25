from typing import Reversible
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(verbose_name="Nombres", max_length=50)
    apellido = models.CharField(verbose_name="Apellidos", max_length=50)
    rut = models.CharField(verbose_name="Rut", max_length=9)
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(verbose_name="Direccion", max_length=50)
    telefono = models.CharField(verbose_name="Telefono", max_length=9)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    MATERIAL = [('1', 'Vidrio'), ('2', 'Metal'),('3', 'Plástico'),]
    tamaño = models.CharField(verbose_name="Tamaño", max_length=10)
    COLORES = [('1', 'Negro'),('2', 'Azul metálico'),('3', 'Rasta'),('4', 'Silver'),('5', 'Gold')]
    colores = models.CharField(verbose_name="Color", choices=COLORES, max_length=1)
    precio = models.CharField(verbose_name="Precio", max_length=10)
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.precio
    
    def get_absolute_url(self):
        return Reversible("producto", args=[str(self.id)])
    

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Producto")
    numero = models.IntegerField(verbose_name="Numero del pedido")
    fecha = models.DateField(verbose_name="Fecha del pedido")
    ESTADO = [('E', 'Envío'), ('R', 'Retiro en tienda')]
    estado = models.CharField(verbose_name="Entrega", choices=ESTADO, max_length=1)
    entrega = models.DateField(verbose_name="Fecha de entrega", null=True, blank=True)

    def get_absolute_url(self):
        return Reversible(args=[str(self.id)])
