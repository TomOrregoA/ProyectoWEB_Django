from django.shortcuts import render, redirect
from .models import Obra, Usuario
from .forms import UsuarioForm, ObraForm



def home(request):
    obras = Obra.objects.all()
    datos = {
        'obras': obras
    }
    return render(request, 'app/index.html', datos)

def editarObra(request):
    return render(request, 'app/editar_obra.html')


def login(request):
    return render(request, 'app/login.html')

def register(request):
    usuarios = Usuario.objects.all()
    datos = {
        'usuarios': usuarios,
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'app/register.html', datos)

def form_obra(request):
    datos = {
        'form': ObraForm()
    }

    if request.method == 'POST':
        formulario = ObraForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Obra Guardada Correctamente"

    return render(request, 'app/form_obra.html', datos)

def form_mod_obra(request, title):
    obra = Obra.objects.get(title=title)
    datos = { 
        'form': ObraForm(instance=obra)
    }
    if request.method == 'POST':
        formulario = ObraForm(data=request.POST,instance=obra)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Obra modificada correctamente"
    return render(request, 'app/form_mod_obra.html', datos)

def form_del_obra(request, title):
    obra = Obra.objects.get(title=title)
    obra.delete()
    return redirect(to="home")

def form_usuario(request):
    return render(request, 'app/form_usuario.html')
