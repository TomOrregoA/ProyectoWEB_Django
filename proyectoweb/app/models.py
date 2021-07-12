from django.db import models

#Modelo para usuarios

class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True, verbose_name='Id de Usuario')
    name = models.CharField(max_length=25, verbose_name='Nombre de Usuario')
    aPaterno = models.CharField(max_length=25, verbose_name='Apellido Paterno')
    aMaterno = models.CharField(max_length=25, null=True, blank=True, verbose_name='Apellido Materno')
    user = models.CharField(max_length=25, unique=True, verbose_name='Usuario')
    password = models.CharField(max_length=25, verbose_name='Password')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Teléfono')
    email = models.CharField(max_length=50, verbose_name='Correo')
    def __str__(self):
        return self.name

#Modelo para categorias

class Categoria(models.Model):
    idCatergoria = models.AutoField(primary_key=True, verbose_name='Id Categoría')
    descripcion = models.CharField(max_length=25, verbose_name='Categoria')
    def __str__(self):
        return self.descripcion

#Modelo para obras

class Obra(models.Model):
    idObra = models.AutoField(primary_key=True, verbose_name='Id de la Obra')
    title = models.CharField(max_length=25, unique=True, verbose_name='Título de Obra')
    price = models.IntegerField(verbose_name='Precio de Obra')
    heigth = models.IntegerField(verbose_name='Alto de Obra')
    width = models.IntegerField(verbose_name='Ancho de Obra')
    year = models.IntegerField(verbose_name='Año de Obra')
    image = models.ImageField(upload_to='gallery', null=True, verbose_name='Imagen de Obra' )
    style = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Estilo de Obra')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Autor de Obra')
    def __str__(self):
        return self.title
