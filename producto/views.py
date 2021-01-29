from django.shortcuts import render
from producto.models import Producto

# Create your views here.

def producto(request):
    productos=Producto.objects.all()
    return render(request, "producto/producto.html", {"productos": productos})