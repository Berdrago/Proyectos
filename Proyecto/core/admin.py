from core.models import Componente, Cuenta, Fabricante, Producto,Cuenta
from django.contrib import admin

# Register your models here.

admin.site.register(Componente)
admin.site.register(Fabricante )
admin.site.register(Producto )
admin.site.register(Cuenta)

