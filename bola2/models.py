from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    tamaño = models.CharField(verbose_name="Tamaño", max_length=20)
    COLOR = [('1','Negro'),('2','Azul'),('3','Rojo'),('4','Verde'),('5','Blanco'),('6','Rosado')]
    color = models.CharField(verbose_name="Color", choices=COLOR, max_length=1)
    MATERIAL = [('1','Plastico'),('2','Vidrio'),('3','Metal')]
    material = models.CharField(verbose_name="Material", choices=MATERIAL, max_length=1)

    def __str__(self):
        return self.nombre
    
class Descripcion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Producto")
    reseña = models.TextField(verbose_name="Reseña")
    
    def __str__(self):
        return self.producto


    
