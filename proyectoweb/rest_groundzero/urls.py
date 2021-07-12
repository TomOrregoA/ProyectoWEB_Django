from django.urls import path
from rest_groundzero import views
from rest_groundzero.viewslogin import login

urlpatterns = [
    path('lista_obras', views.lista_obras, name='lista_obras'),
    path('detalle_obra/<title>', views.detalle_obra, name='detalle_obra'),
    path('login', login, name='login')
]
