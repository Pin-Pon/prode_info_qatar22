from re import template
from django.shortcuts import render

from equipos.models import Equipo

def inicio(request):
    template_name="inicio.html"
    usuario={
        "nombre":"TAMARA",
        "apellido":"HIDAlGO"
    }
    equipos =Equipo.objects.all()
    print(equipos)
    ctx={
        'equipos' : equipos
       # 'user_dict': usuario
    }
    return render(request, template_name, ctx)
def login(request):
    return render(request,"login.html",{})    
 