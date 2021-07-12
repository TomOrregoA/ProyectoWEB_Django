from django import forms
from django.forms import ModelForm
from .models import Usuario, Obra

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'aPaterno', 'aMaterno', 'user', 'password', 'phone', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'aPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'aMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['title', 'price', 'heigth', 'width', 'year', 'image', 'style', 'autor']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'heigth': forms.TextInput(attrs={'class': 'form-control'}),
            'width': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }