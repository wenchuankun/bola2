from django.db import models

# Create your models here.
<<<<<<< HEAD

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
=======
<<<<<<< HEAD
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    tamaño = models.CharField(verbose_name="Tamaño", max_length=20)
    COLOR = [('1','Negro'),('2','Azul'),('3','Rojo'),('4','Verde'),('5','Blanco'),('6','Rosado')]
    color = models.CharField(verbose_name="Color", choices=COLOR, max_length=1)
    MATERIAL = [('1','Plastico'),('2','Vidrio'),('3','Metal')]
    material = models.CharField(verbose_name="Material", choices=MATERIAL, max_length=1)
    precio = models.IntegerField(verbose_name="Precio", max_length=50)

    def __str__(self):
        return self.nombre
    
class Descripcion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Producto")
    reseña = models.TextField(verbose_name="Reseña")
    
    def __str__(self):
        return self.producto


    
>>>>>>> 1ead3ebdbf2452d969121d1f744324523091294a
