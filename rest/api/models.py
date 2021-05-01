from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class libro (models.Model):
    id          = models.AutoField    (primary_key=True ,verbose_name='Id del  libro:')
    nombre      = models.CharField    (max_length=99, verbose_name='Nombre del Libro:')
    autor       = models.CharField    (null=True, max_length=99,verbose_name='Autor de libro:')
    sinopsis    = models.TextField    (null=True, verbose_name='Sinopsis de Libros:')
    precio      = models.IntegerField (default=0 ,verbose_name='Precio Libro:')
    stock       = models.IntegerField (default=0, verbose_name='Stock de libro: ')
    publicacion = models.DateField    (null=True,verbose_name=' Fecha de publicacion Libro:')
class Cuenta (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) 
    libro   = models.ManyToManyField(libro)
