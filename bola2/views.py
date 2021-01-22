from django.shortcuts import render
from .models import Cliente, Producto, Pedido

# Create your views here.
def index(request):
    clientes = Cliente.object.all().count()
    productos = Producto.object.all().count()
    pedidos = Pedido.object.all().count()
    
    return render(
        request,
        'index.html',
        context={'clientes':clientes,'productos':productos,'pedidos':pedidos}
    )