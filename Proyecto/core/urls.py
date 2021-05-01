from core.views import acces, administrador, bicicletas, carro, deslogeocliente, deslogeosupervisor, inicio, logeandocliente, logeandosupervisor, nosotros, registrandocliente, registrandosupervisor, registro, servicios
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',inicio,name  = 'inicio'),
    path('registro/',registro,name  = 'registro'),
    path('acces/',acces,name  = 'acces'),
    path('bicicletas/',bicicletas,name  = 'bicicletas'),
    path('carro/',carro,name  = 'carro'),
    path('nosotros/',nosotros,name  = 'nosotros'),
    path('servicios/',servicios,name  = 'servicios'),
    path('logeandocliente/',logeandocliente,name  = 'logeandocliente'),
    path('logeandosupervisor/',logeandosupervisor,name  = 'logeandosupervisor'),
    path('logeandocliente/deslogeocliente /',deslogeocliente ,name  = 'deslogeocliente '),
    path('logeandosupervisor/deslogeosupervisor/',deslogeosupervisor,name  = 'deslogeosupervisor'),
    path('registrandocliente/',registrandocliente,name  = 'registrandocliente'),
    path('administrador/',administrador,name  = 'administrador'),
    path('registrandosupervisor/',registrandosupervisor,name  = 'registrandosupervisor')
    

]
