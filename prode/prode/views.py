from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from equipos.models import Equipo

def inicio(request):
    template_name="inicio.html"
    
    equipos =Equipo.objects.filter(nombre="Argentina") 
    Equipo.objects.create(
        nombre="Alemania"
    )# query > Consultas mediante orm
   
    ctx={
        'equipos' : equipos,
         'nombre' : "Octavio"
    }
    return render(request, template_name, ctx)

# def login(request):
#     return render(request,"login.html",{})  

# ef mis_grupos(request):
#     return render(request,"mis_grupos.html",{})d
class MisGrupos(TemplateView):
    template_name = "mis_grupos.html"