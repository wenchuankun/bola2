from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(verbose_name="Nombre", max_length=50)
    direccion=models.CharField(verbose_name="Direccion", max_length=50)
    email=models.EmailField(verbose_name="Email")
    Telefono=models.CharField(verbose_name="Telefono", max_length=9)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    COLORES = [('1', 'Rojo'), ('2', 'Negro'),
                  ('3', 'Azul'), ('4', 'Blanco')]
    colores = models.CharField(verbose_name="Colores", choices=COLORES, max_length=1)
    precio = models.CharField(verbose_name="Precio", max_length=10)
    tamaño = models.CharField(verbose_name="Tamaño", max_length=10)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=100)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    numero = models.IntegerField(verbose_name="Numero del pedido")
    fecha = models.DateField(verbose_name="Fecha del pedido")
    ESTADO = [('E', 'Entregado'), ('P', 'Pendiente')]
    estado = models.CharField(verbose_name="Estado",choices=ESTADO, max_length=1)

    def __str__(self):
        return self.numero, self.estado



