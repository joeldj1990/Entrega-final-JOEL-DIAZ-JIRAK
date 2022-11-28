from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .forms import Armazones_Formulario, Sol_Formulario, Lentes_Formulario, User_Edit_Form, User_Profile_Form, User_Register_Form
from .models import Armazones, Lentes_Sol, Cristales, Avatar

# Create your views here.


@login_required
def avatar(request):
    user = User.objects.get(username=request.user)
    imagen = Avatar.objects.filter(user=user)
    contexto = {
        "imagen": imagen,
    }
    return contexto


def inicio(request):
    return render(request, "inicio.html")


@staff_member_required(login_url="/app1/acceso-denegado")
def armazones(request):
    lista = Armazones.objects.all()
    return render(request, "armazones.html", {"armazones": lista})


@staff_member_required(login_url="/app1/acceso-denegado")
def anteojos_sol(request):
    lista = Lentes_Sol.objects.all()
    return render(request, "anteojos-sol.html", {"anteojos_sol": lista})


@staff_member_required(login_url="/app1/acceso-denegado")
def lentes(request):
    lista = Cristales.objects.all()
    return render(request, "lentes.html", {"lentes": lista})


def horario(request):
    return render(request, "horario.html")


def preguntas(request):
    return render(request, "preguntas-frecuentes.html")


@staff_member_required(login_url="/app1/acceso-denegado")
def armazones_formulario(request):
    if request.method == 'POST':
        formulario = Armazones_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            armazones_formulario = Armazones(material=data['material'], marca=data['marca'], color=data['color'], tamagno=data['tamaño'], precio=data['precio'], codigo=data['código'], foto=data['foto'], medidas=data['medidas'], tipo=data['tipo'], peso=data['peso'], estilo=data['estilo'], fecha=data['fecha'])
            armazones_formulario.save()

            return redirect('Armazones')
        
    else:
        formulario = Armazones_Formulario()

    return render(request, 'armazones-formulario.html', {'formulario': formulario})


@staff_member_required(login_url="/app1/acceso-denegado")
def sol_formulario(request):
    if request.method == 'POST':
        formulario = Sol_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            sol_formulario = Lentes_Sol(material=data['material'], marca=data['marca'], color_armazon=data['color_armazón'], color_lente=data['color_lente'], tamagno=data['tamaño'], precio=data['precio'], codigo=data['código'], foto=data['foto'], medidas=data['medidas'], tipo=data['tipo'], peso=data['peso'], polarizado=data['polarizado'], antireflejo=data['antireflejo'], estilo=data['estilo'], fecha=data['fecha'])
            sol_formulario.save()

            return redirect('Anteojos_Sol')
        
    else:
        formulario = Sol_Formulario()

    return render(request, 'sol-formulario.html', {'formulario': formulario})


@staff_member_required(login_url="/app1/acceso-denegado")
def lentes_formulario(request):
    if request.method == 'POST':
        formulario = Lentes_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            lentes_formulario = Cristales(material=data['material'], marca=data['marca'], color=data['color'], graduacion=data['graduación'], precio=data['precio'], codigo=data['código'], foto=data['foto'], laboratorio=data['laboratorio'], duracion=data['duración'], prescripcion=data['prescripción'], fecha=data['fecha'])
            lentes_formulario.save()

            return redirect('Lentes')
        
    else:
        formulario = Lentes_Formulario()

    return render(request, 'lentes-formulario.html', {'formulario': formulario})


def busqueda_codigo(request):
    return render(request, 'busqueda-codigo.html')


def buscar(request):
    if "q" in request.GET:
        q = request.GET["q"]
        multiple_q = Q(Q(marca__icontains=q) | Q(color__icontains=q) | Q(material__icontains=q) | Q(tamagno__icontains=q) | Q(tipo__icontains=q))
        multiple_q2 = Q(Q(marca__icontains=q) | Q(color_armazon__icontains=q) | Q(color_lente__icontains=q) | Q(material__icontains=q) | Q(tamagno__icontains=q) | Q(tipo__icontains=q))
        multiple_q3 = Q(Q(marca__icontains=q) | Q(color__icontains=q) | Q(material__icontains=q) | Q(laboratorio__icontains=q) | Q(duracion__icontains=q) | Q(prescripcion__icontains=q))
        armazon = Armazones.objects.filter(multiple_q)
        sol= Lentes_Sol.objects.filter(multiple_q2)
        lente = Cristales.objects.filter(multiple_q3)
    return render(request, 'resultado-busqueda.html', {"armazones": armazon, "anteojos_sol": sol, "lentes": lente})


@staff_member_required(login_url="/app1/acceso-denegado")
def eliminar_armazones(request, id):
    if request.method == 'POST':
        armazon = Armazones.objects.get(id=id)
        armazon.delete()
        armazones = Armazones.objects.all()
        return render(request, 'armazones.html', {"armazones": armazones})


@staff_member_required(login_url="/app1/acceso-denegado")
def eliminar_sol(request, id):
    if request.method == 'POST':
        sol = Lentes_Sol.objects.get(id=id)
        sol.delete()
        soles = Lentes_Sol.objects.all()
        return render(request, 'anteojos-sol.html', {"anteojos_sol": soles})


@staff_member_required(login_url="/app1/acceso-denegado")
def eliminar_lentes(request, id):
    if request.method == 'POST':
        lente = Cristales.objects.get(id=id)
        lente.delete()
        lentes = Cristales.objects.all()
        return render(request, 'lentes.html', {"lentes": lentes})


@staff_member_required(login_url="/app1/acceso-denegado")
def editar_armazones(request, id):
    armazon = Armazones.objects.get(id=id)
    if request.method == 'POST':
        formulario = Armazones_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            armazon.marca = data["marca"]
            armazon.color = data["color"]
            armazon.material = data["material"]
            armazon.tamagno = data["tamaño"]
            armazon.precio = data["precio"]
            armazon.codigo = data["código"]
            armazon.foto = data["foto"]
            armazon.medidas = data["medidas"]
            armazon.tipo = data["tipo"]
            armazon.peso = data["peso"]
            armazon.estilo = data["estilo"]
            armazon.fecha = data["fecha"]
            armazon.save()

            return redirect('Armazones')
        
    else:
        formulario = Armazones_Formulario(initial={
            "marca": armazon.marca,
            "color": armazon.color,
            "material": armazon.material,
            "tamaño": armazon.tamagno,
            "precio": armazon.precio,
            "código": armazon.codigo,
            "foto": armazon.foto,
            "medidas": armazon.medidas,
            "tipo": armazon.tipo,
            "peso": armazon.peso,
            "estilo": armazon.estilo,
            "fecha": armazon.fecha
        })

    return render(request, 'editar-armazon.html', {'formulario': formulario, "id": armazon.id, "foto": armazon.foto})


@staff_member_required(login_url="/app1/acceso-denegado")
def editar_soles(request, id):
    sol = Lentes_Sol.objects.get(id=id)
    if request.method == 'POST':
        formulario = Sol_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            sol.marca = data["marca"]
            sol.color_armazon = data["color_armazón"]
            sol.color_lente = data["color_lente"]
            sol.material = data["material"]
            sol.tamagno = data["tamaño"]
            sol.precio = data["precio"]
            sol.codigo = data["código"]
            sol.foto = data["foto"]
            sol.medidas = data["medidas"]
            sol.tipo = data["tipo"]
            sol.peso = data["peso"]
            sol.polarizado = data["polarizado"]
            sol.antireflejo = data["antireflejo"]
            sol.estilo = data["estilo"]
            sol.fecha = data["fecha"]
            sol.save()

            return redirect('Anteojos_Sol')
        
    else:
        formulario = Sol_Formulario(initial={
            "marca": sol.marca,
            "color_armazón": sol.color_armazon,
            "color_lente": sol.color_lente,
            "material": sol.material,
            "tamaño": sol.tamagno,
            "precio": sol.precio,
            "código": sol.codigo,
            "foto": sol.foto,
            "medidas": sol.medidas,
            "tipo": sol.tipo,
            "peso": sol.peso,
            "polarizado": sol.polarizado,
            "antireflejo": sol.antireflejo,
            "estilo": sol.estilo,
            "fecha": sol.fecha
        })

    return render(request, 'editar-sol.html', {'formulario': formulario, "id": sol.id, "foto": sol.foto})


@staff_member_required(login_url="/app1/acceso-denegado")
def editar_lentes(request, id):
    lente = Cristales.objects.get(id=id)
    if request.method == 'POST':
        formulario = Lentes_Formulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            lente.marca = data["marca"]
            lente.color = data["color"]
            lente.material = data["material"]
            lente.graduacion = data["graduación"]
            lente.precio = data["precio"]
            lente.codigo = data["código"]
            lente.foto = data["foto"]
            lente.laboratorio = data["laboratorio"]
            lente.duracion = data["duración"]
            lente.prescripcion = data["prescripción"]
            lente.fecha = data["fecha"]
            lente.save()

            return redirect('Lentes')
        
    else:
        formulario = Lentes_Formulario(initial={
            "marca": lente.marca,
            "color": lente.color,
            "material": lente.material,
            "graduación": lente.graduacion,
            "precio": lente.precio,
            "código": lente.codigo,
            "foto": lente.foto,
            "laboratorio": lente.laboratorio,
            "duración": lente.duracion,
            "prescripción": lente.prescripcion,
            "fecha": lente.fecha
        })

    return render(request, 'editar-lente.html', {'formulario': formulario, "id": lente.id, "foto": lente.foto})


class Armazones_List(ListView):
    model = Armazones
    template_name = 'armazones-list.html'
    context_object_name = 'armazones'


class Armazones_Detail(DetailView):
    model = Armazones
    template_name = 'armazones-detail.html'
    context_object_name = 'armazon'


class Sol_List(ListView):
    model = Lentes_Sol
    template_name = 'sol-list.html'
    context_object_name = 'anteojos_sol'


class Sol_Detail(DetailView):
    model = Lentes_Sol
    template_name = 'sol-detail.html'
    context_object_name = 'sol'


class Lentes_List(ListView):
    model = Cristales
    template_name = 'lentes-list.html'
    context_object_name = 'lentes'


class Lentes_Detail(DetailView):
    model = Cristales
    template_name = 'lentes-detail.html'
    context_object_name = 'lente'


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            formulario = AuthenticationForm(request, data=request.POST)
            if formulario.is_valid():
                data = formulario.cleaned_data
                usuario = data["username"]
                password = data["password"]
                user = authenticate(username=usuario, password=password)
                if user:
                    login(request, user)
                    return render(request,"login-mensaje.html", {"mensaje": f'Bienvenido {usuario}'})
                else:
                    return render(request,"login-mensaje.html", {"mensaje": f'Error, datos incorrectos'})
            return render(request,"login-mensaje.html", {"mensaje": f'Error, formulario invalido'})
        else:
            formulario = AuthenticationForm()
            return render(request, 'login.html', {'formulario': formulario})
    else: 
        return render(request, "acceso-denegado.html", {"mensaje": f'Usted ya está logueado'})


def registrar(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            formulario = User_Register_Form(request.POST)
            if formulario.is_valid():
                usuario = formulario.cleaned_data["username"]
                formulario.save()
                return render(request, 'login-mensaje.html', {"mensaje": f'Usuario {usuario} creado con éxito'})
            else:
                return render(request, 'login-mensaje.html', {"mensaje": f'Error al crear el usuario'})
        else:
            formulario = User_Register_Form()
        return render(request, 'registro-usuario.html', {'formulario': formulario})
    return render(request, "acceso-denegado.html", {"mensaje": f'No puede crear un nuevo usuario mientras está logueado'})


def acceso_denegado(request):
    return render(request, 'acceso-denegado.html', {"mensaje": f'No posee los permisos necesarios para ver esta sección'})

@login_required(login_url="/app1/acceso-denegado")
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = User_Edit_Form(request.POST)
        perfil = User_Profile_Form(request.POST, request.FILES, instance=request.user.avatar)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            perfil.save()

            return render(request, 'login-mensaje.html', {"mensaje": f'Datos actualizados'})
        return render(request, 'acceso-denegado.html', {'mensaje': f'Las constraseñas no coinciden'}) 
        
    else:
        formulario = User_Edit_Form(instance=request.user)
        perfil = User_Profile_Form(instance=request.user.avatar)

    return render(request, 'editar-perfil.html', {'formulario': formulario, 'perfil': perfil})


def sin_paginas(request):
    return render(request, 'acceso-denegado.html', {"mensaje": f'Sin páginas para mostrar aún'})


def about(request):
    return render(request, "about.html")


@login_required(login_url="/app1/acceso-denegado")
def cambiar_avatar(request):
    usuario = request.user
    if request.method == 'POST':
        perfil = User_Profile_Form(request.POST, request.FILES, instance=request.user.avatar)
        if perfil.is_valid():
            data = perfil.cleaned_data
            usuario.imagen = data["imagen"]
            usuario.save()
            perfil.save()

            return render(request, 'login-mensaje.html', {"mensaje": f'Avatar cambiado con éxito'})
        return render(request, 'acceso-denegado.html', {'mensaje': f'Error'}) 
        
    else:
        perfil = User_Profile_Form(instance=request.user.avatar)

    return render(request, 'editar-perfil.html', {'perfil': perfil})


@login_required(login_url="/app1/acceso-denegado")
def contacto(request):
    if request.method == 'POST':
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["optieyes777@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'gracias.html')
    return render(request, 'contacto.html')
