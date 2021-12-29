from django.shortcuts import render
from django.http import HttpResponse

from AppCovid.models import Guantes, Barbijos, Oximetros
# Create your views here.

def inicio(request):

    return render(request, "AppCovid/inicio.html")

def guantes(request):

    return render(request, "AppCovid/guantes.html")

def barbijos(request):
    
    return render(request, "AppCovid/barbijos.html")

def oximetros(request):
    
    return render(request, "AppCovid/oximetros.html")

def barbijosFormulario(request):
    return render(request, "AppCovid/barbijosFormulario.html")

