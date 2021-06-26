from django.shortcuts import render
from .models import Obra, Usuario
from .forms import UsuarioForm

def home(request):
    obras = Obra.objects.all()
    datos = {
        'obras': obras
    }
    return render(request, 'app/index.html', datos)

def login(request):
    return render(request, 'app/login.html')

def register(request):
    datos = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardador Correctamente"

    return render(request, 'app/register.html', datos)