from re import template
from django.shortcuts import render


def inicio(request):
    template_name="inicio.html"
    usuario={
        "nombre":"TAMARA",
        "apellido":"HIDAlGO"
    }
    ctx={
        "user_dict": usuario
    }
    return render(request, template_name, ctx)
 