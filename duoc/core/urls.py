from core.views import Admin,  CPU, Deslogeo, EliminarProducto, GPU, HDD, Logeando, M2, ModificarProducto, PSU, RAM, Registrando, SSD, Signin, Signup,home,MB
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',home,name  = 'home'),
    path('mb',MB,name = 'MB'),
    path('cpu',CPU,name   = 'CPU'),
    path('hdd',HDD,name   = 'HDD'),
    path('gpu',GPU,name   = 'GPU'),
    path('m2',M2,name     = 'M2'),
    path('psu',PSU,name   = 'PSU'),
    path('ram',RAM,name   = 'RAM'),
    path('ssd',SSD,name   = 'SSD'),
    path('Admin',Admin,name   = 'Admin'),
    path('signin/',Signin,name   = 'Signin'),
    path('signin/Logeando/',Logeando,name    =  'Logeando'),
    path('signin/deslogeo/',Deslogeo ,name   = 'Deslogeo'),
    path('signup/Registrando/',Registrando ,name   = 'Registrando'),
    path('signup',Signup,name   = 'Signup'),
    path('adopta/perros/form/mod/modificando/', ModificarProducto, name='ModificarPerro'),
    path('EliminarProducto/<int:idProducto>/', EliminarProducto,   name='EliminarProducto')
    
]
