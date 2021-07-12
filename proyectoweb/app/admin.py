from django.contrib import admin
from .models import Usuario, Obra, Categoria
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Obra)