from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"main/index.html")

def contacto(request):
    return render(request,"main/contacto.html")

def donar(request):
    return render(request,"main/donar.html")

def noticias(request):
    return render(request,"main/noticias.html")

def quienes_somos(request):
    return render(request,"main/quienessomos.html")
