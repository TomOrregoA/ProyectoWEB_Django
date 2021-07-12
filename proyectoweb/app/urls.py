from django.urls import path
from .views import home, login, register, form_obra, form_mod_obra, form_del_obra, form_usuario, editarObra

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('subir-obra/', form_obra, name='form_obra'),
    path('crear-usuario/', form_usuario, name='form_usuario'),
    path('editar-obra/', editarObra, name='editarObra'),
    path('modificar-obra/<title>', form_mod_obra, name='form_mod_obra'),
    path('eliminar-obra/<title>', form_del_obra, name='form_del_obra'),
]