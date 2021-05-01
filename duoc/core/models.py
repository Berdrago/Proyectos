from django.db import models

# Create your models here.


class Componente(models.Model):
    idComponente = models.AutoField (primary_key=True ,verbose_name="Id del componente")
    nombreComponente = models.CharField(max_length=99 , verbose_name="Nombre del Componente")

    def __str__(self) :
        return self.nombreComponente

class Fabricante (models.Model):
    idFabricante = models.AutoField (primary_key=True ,verbose_name="Id del Fabricante ")
    nombreFabricante = models.CharField(max_length=99 , verbose_name="Nombre del Fabricate ")
    def __str__(self) :
        return self.nombreFabricante 

class Producto (models.Model):
    idProducto = models.AutoField (primary_key=True ,verbose_name="Id del Producto ")
    nombreProducto= models.CharField(max_length=99 , verbose_name="Nombre del Producto ")
    fabricante = models.ForeignKey (Fabricante ,null=True, blank=True, on_delete=models.CASCADE )
    componente = models.ForeignKey (Componente ,null=True, blank=True, on_delete=models.CASCADE )
    precio = models.IntegerField (default=0)
    stock = models.IntegerField (default=0)
    def ruta_imagen (self,filename ):
        return f'producto/{self.idProducto}/imagenes/{filename}'  

    imagen = models.ImageField( upload_to  = ruta_imagen  ,null=True, blank=True  )
    def __str__(self) :
        return self.nombreProducto 










