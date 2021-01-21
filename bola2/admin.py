from django.contrib import admin
from bola2.models import Cliente, Producto, Galeria


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

