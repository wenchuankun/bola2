from django.contrib import admin
<<<<<<< HEAD
from bola2.models import Cliente, Producto, Galeria


=======
from .models import models
>>>>>>> 1ead3ebdbf2452d969121d1f744324523091294a
# Register your models here.

class ClientesAdmin (admin.ModelAdmin):
    list_display=("nombre", "direccion", "Telefono")
    search_fields=("nombre", "Telefono")

class ProductoAdmin (admin.ModelAdmin):
    list_display=("producto", "color", "precio")
    search_fields=("producto", "color")

class GaleriaAdmin (admin.ModelAdmin):
    list_display=("nombre_imagen")




admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto)
admin.site.register(Galeria)

