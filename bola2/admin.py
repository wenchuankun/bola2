from django.contrib import admin
from bola2.models import Cliente, Producto, Pedido, Galeria
class ClientesAdmin (admin.ModelAdmin):
    list_display=("nombre", "direccion", "Telefono")
    search_fields=("nombre", "Telefono")

class ProductoAdmin (admin.ModelAdmin):
    list_display=("nombre", "colores", "precio")
    search_fields=("nombre", "colores")

class PedidoAdmin (admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("numero", "fecha")


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Galeria)


