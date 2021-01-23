from django.contrib import admin
from django.db.models.fields import files
from .models import Cliente, Producto, Pedido

@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    list_display=("nombre",  "direccion", "email", "Telefono")
    fields=["nombre",  "direccion", "email", "Telefono"]

@admin.register(Producto)
class ProductoAdmin (admin.ModelAdmin):
    list_display=("nombre", "colores", "precio")
    fields=["nombre", "colores", "tamaño", "descripcion",  "precio"]

@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):
    list_filter=("numero", "fecha", "estado")






