from core.forms import formAgregar
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  
from django.shortcuts import redirect, render
from .models import Fabricante, Producto
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'home.html',contexto)

def Admin(request):
    idFabricantes = request.POST.get('fabricante', '')
    nombreFabricante = Fabricante.objects.get(idFabricante = idFabricantes)
    
    idProducto         =   request.POST.get('idProducto ', '')
    nombreProducto     =   request.POST.get('nombreProducto', '')       
    imagen             =   request.FILES.get('imagen ', '')

    producto = Producto.objects.get(idProducto=idProducto)
    producto .nombreProducto  = nombreProducto 
    producto .fabricante = nombreFabricante

    if(imagen != ''):
        producto .imagen = imagen
        
    producto.save()

    producto = Producto.objects.all()
    datos = {
        'producto':producto,
        'form' : formAgregar()
    }
    if request.method=='POST':
        formulario = formAgregar(request.POST,request.FILES)
        if formulario.is_valid :
                formulario.save()
                datos   ['mensaje'] = "Los datos se guardaron correctamente "

    return render(request,'Admin.html',datos)

def MB(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'MB.html',contexto)

def CPU(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'CPU.html',contexto)

def GPU(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'GPU.html',contexto)

def HDD(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'HDD.html',contexto)

def M2(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'M2.html',contexto)

def PSU(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'PSU.html',contexto)

def RAM(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'RAM.html',contexto)

def SSD(request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'SSD.html',contexto)
def Signin(request):
    contexto = {}
    return render(request,'Signin.html',{})

def Logeando (request):
    username = request.POST.get('Usuario','')
    password = request.POST.get('password','')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('Signin')

def Deslogeo (request): 
    logout(request)
    return redirect('home')

def Signup (request):
    return render(request,'Signup.html',{})


def Registrando(request): 
    usuario = request.POST.get('usuario','') 
    password = request.POST.get('password2','')
    email = request.POST.get('Email','')
    user = User.objects.create_user(usuario,email,password)
    user.save()
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('Signin')

def ModificarProducto(request):
    idFabricantes = request.POST.get('fabricante', '')
    nombreFabricante = Fabricante.objects.get(idFabricante = idFabricantes)
    
    idProducto         =   request.POST.get('idProducto ', '')
    nombreProducto     =   request.POST.get('nombreProducto', '')       
    imagen             =   request.FILES.get('imagen ', '')

    producto = Producto.objects.get(idProducto=idProducto)
    producto .nombreProducto  = nombreProducto 
    producto .fabricante = nombreFabricante

    if(imagen != ''):
        producto .imagen = imagen
        
    producto.save()

    return redirect('Admin')

def EliminarProducto (request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto .delete()

    return redirect('Admin')
def imagen (request):
    productos =  Producto.objects.filter(stock__gte=0).order_by('-idProducto') 
    contexto=  {
        'productos':productos}
    return render(request,'admin.html',contexto)
def FormularioProducto(request, idProducto):
    productos    = Producto.objects.get(idProducto=idProducto)
    fabricantes = Fabricante.objects.all()
    contexto = {'fabricantes': fabricantes, 'productos': productos}

    return render(request, 'admin.html', contexto)




    



