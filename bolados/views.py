from django.shortcuts import render, HttpResponse


# Create your views here.

def Inicio(request):
    return render( request, "bolados/Inicio.html")

def Producto(request):
    return render( request, "bolados/Producto.html")

def Pedido(request):
    return render( request, "bolados/Pedido.html")

def Cliente(request):
    return render( request, "bolados/Cliente.html")

def Login(request):
    return render( request, "bolados/Login.html")