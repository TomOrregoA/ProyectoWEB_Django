from django.db import models

#Modelo para usuarios

class Usuario(models.Model):
    idUser = models.IntegerField(primary_key=True, verbose_name='Nombre de Usuario')
    name = models.CharField(max_length=25, verbose_name='Nombre de Usuario')
    aPaterno = models.CharField(max_length=25, verbose_name='Apellido Paterno')
    aMaterno = models.CharField(max_length=25, null=True, blank=True, verbose_name='Apellido Materno')
    user = models.CharField(max_length=25, verbose_name='Usuario')
    password = models.CharField(max_length=25, verbose_name='Password')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Teléfono')
    email = models.CharField(max_length=50, verbose_name='Correo')

    def __str__(self):
        return self.name

#Modelo para obras

class Obra(models.Model):
    idObra = models.IntegerField(primary_key=True, verbose_name='Id de la Obra')
    title = models.CharField(max_length=25, verbose_name='Título de Obra')
    price = models.IntegerField(verbose_name='Precio de Obra')
    style = models.CharField(max_length=25, verbose_name='Estilo de Obra')
    heigth = models.IntegerField(verbose_name='Alto de Obra')
    width = models.IntegerField(verbose_name='Ancho de Obra')
    year = models.IntegerField(verbose_name='Año de Obra')
    image = models.ImageField(upload_to='images/gallery/')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
