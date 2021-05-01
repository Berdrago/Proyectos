"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.login.LoginAPI import LoginAPI,     LogoutAPI
from api.Cuenta.CuentaAPI import CuentaAPI
from api.usuario.UsuarioAPI import UsuarioAPI
from api.Libro.LibroAPI import LibroAPI
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #Libros CRUD
    path('api/v1/libro/select/<int:id>/',   LibroAPI.as_view(), name='LibroAPI'),#URL GET
    path('api/v1/libro/create/',            LibroAPI.as_view(), name='LibroAPI'),#URL POST
    path('api/v1/libro/update/<int:id>/',   LibroAPI.as_view(), name='LibroAPI'),#URL PUT
    path('api/v1/libro/delete/<int:id>/',   LibroAPI.as_view(), name='LibroAPI'), #URL DELETE

    #Usuarios
    path('api/v1/usuario/',UsuarioAPI.as_view(), name=' UsuarioAPI'), 

    #Cuenta
    path('api/v1/cuenta/<int:id>/',CuentaAPI.as_view(), name=' CuentaAPI'), 

    #Login 
    path('api/v1/login/',LoginAPI.as_view(), name=' LoginAPI'), 

    #Logout
    path('api/v1/logout/',LogoutAPI.as_view(), name=' LoginAPI'), 
    
] 

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
