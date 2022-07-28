from re import template
from django.shortcuts import render

from equipos.models import Equipo

def inicio(request):
    template_name="inicio.html"
    usuario={
        "nombre":"TAMARA",
        "apellido":"HIDAlGO"
    }
    equipos =Equipo.objects.all() # query > Consultas mediante orm
    print("*************************")
    print(equipos,usuario)
    print("*************************")
    ctx={
        'equipos' : equipos,
        'user_dict': usuario
    }
    return render(request, template_name, ctx)
def login(request):
    return render(request,"login.html",{})    
def mis_grupos(request):
    return render(request,"mis_grupos.html",{})