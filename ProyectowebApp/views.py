from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectowebApp/home.html")



def login(request):
    return render(request, "ProyectowebApp/login.html")




