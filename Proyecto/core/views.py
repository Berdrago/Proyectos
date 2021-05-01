from core.models import Cuenta
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  
from django.shortcuts import redirect, render
from django.contrib.auth.models import User




def inicio(request):
    contexto = {}
    return render(request,'inicio.html',{})

def administrador (request):
    contexto = {}
    return render(request,'administrador.html',{})
    
def registro (request):
    contexto = {}
    return render(request,'registro.html',{})
def acces (request):
    contexto = {}
    return render(request,'acces.html',{})
def bicicletas  (request):
    contexto = {}
    return render(request,'bicicletas.html',{})
def carro (request):
    contexto = {}
    return render(request,'carro.html',{})
def nosotros (request):
    contexto = {}
    return render(request,'nosotros.html',{})
def servicios (request):
    contexto = {}
    return render(request,'servicios.html',{})
    
def logeandocliente (request):
    username = request.POST.get('usuario','')
    password = request.POST.get('clave','')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('inicio')
    else:
        return redirect('registro')
def logeandosupervisor(request):
    username = request.POST.get('supervisor','')
    password = request.POST.get('clave2','')
    codigo   = request.POST.get('codigo','')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        usuario  = User.objects.get(username=username)
        cuenta   = Cuenta.objects.get(usuario=usuario)
        if cuenta.codigo==int(codigo)  or codigo=='':
            login(request, user)
            return redirect('inicio')
        else:
            return redirect('registro')
    else:
        return redirect('registro')

def deslogeocliente (request): 
    logout(request)
    return redirect('inicio')

def deslogeosupervisor (request): 
    logout(request)
    return redirect('inicio')

def registrandocliente(request): 
    usuario = request.POST.get('nombre','')
    email = request.POST.get('email','')
    password = request.POST.get('clave2','')
    user = User.objects.create_user(usuario,email,password)
    user.save()
    if user is not None:
        login(request, user)
        return redirect('inicio')
    else:
        return redirect('registro')
def registrandosupervisor(request): 
    usuario2 = request.POST.get('usuario','')
    email2 = request.POST.get('email','')
    password2 = request.POST.get('password2','')
    user2 = User.objects.create_user(usuario2 ,email2,password2)
    user2.save()
    Cuenta(usuario= user2,codigo=1369).save()
    if user2 is not None:
        login(request, user2)
        return redirect('inicio')
    else:
        return redirect('registro')


    



