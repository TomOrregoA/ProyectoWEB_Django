from django import forms
from django.forms import ModelForm
from .models import Usuario, Obra

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['idUser', 'name', 'aPaterno', 'aMaterno', 'user', 'password', 'phone', 'email']