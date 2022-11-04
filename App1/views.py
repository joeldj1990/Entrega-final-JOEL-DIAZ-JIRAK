from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template, loader

from .forms import Sol_Formulario, Lentes_Formulario
from .models import Armazones, Lentes_Sol, Cristales

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def armazones(request):
    lista = Armazones.objects.all()
    return render(request, "armazones.html", {"armazones": lista})


def anteojos_sol(request):
    lista = Lentes_Sol.objects.all()
    return render(request, "anteojos-sol.html", {"anteojos_sol": lista})


def lentes(request):
    lista = Cristales.objects.all()
    return render(request, "lentes.html", {"lentes": lista})


def horario(request):
    return render(request, "horario.html")


def preguntas(request):
    return render(request, "preguntas-frecuentes.html")


def armazones_formulario(request):
    if request.method == 'POST':
        armazones = Armazones(material=request.POST['material'], marca=request.POST['marca'], color=request.POST['color'], tamagno=request.POST['tamagno'], precio=request.POST['precio'], codigo=request.POST['codigo'])
        armazones.save()

        return redirect('Armazones')
        

    return render(request, 'armazones-formulario.html')


def sol_formulario(request):
    if request.method == 'POST':
        formulario = Sol_Formulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            sol_formulario = Lentes_Sol(material=data['material'], marca=data['marca'], color_armazon=data['color_armazón'], color_lente=data['color_lente'], tamagno=data['tamaño'], precio=data['precio'], codigo=data['código'])
            sol_formulario.save()

            return redirect('Anteojos_Sol')
        
    else:
        formulario = Sol_Formulario()

    return render(request, 'sol-formulario.html', {'formulario': formulario})


def lentes_formulario(request):
    if request.method == 'POST':
        formulario = Lentes_Formulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            lentes_formulario = Cristales(material=data['material'], marca=data['marca'], color=data['color'], graduacion=data['graduación'], precio=data['precio'], codigo=data['código'])
            lentes_formulario.save()

            return redirect('Lentes')
        
    else:
        formulario = Lentes_Formulario()

    return render(request, 'lentes-formulario.html', {'formulario': formulario})


def busqueda_codigo(request):
    return render(request, 'busqueda-codigo.html')


def buscar(request):
    codigo = request.GET["codigo"]
    armazon = Armazones.objects.filter(codigo = codigo)
    return render(request, 'resultado-busqueda.html', {"armazones": armazon, "codigo": codigo})