from django.shortcuts import render, HttpResponse
from django.db import reset_queries
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

