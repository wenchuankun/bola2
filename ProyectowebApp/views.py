from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, "ProyectowebApp/home.html")

def login(request):
    return render(request, "ProyectowebApp/registration/login.html")

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "hom.html" 


