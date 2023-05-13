from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Servicios
from .forms import UserRegisterForm, UserEditForm, ContactForm
from Producto.models import Producto, Categoria

# Create your views here.

def inicio(request):
    
    productos = Producto.objects.all()
    return render(request, 'inicio.html')

def login_request(request):
    
    if request.method == 'POST':
            
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            usuario = data['username']
            contra = data['password']
            
            user = authenticate(username=usuario, password=contra)
            
            if user:
                
                login(request, user)
                
                return redirect('Inicio')
            
            else:
                
                messages.error(request, "Usuario no válido")
        
        else:
            
            messages.error(request, "Información incorrecta")
    
    else:
    
        form = AuthenticationForm()
    
        return render(request, "login.html", {'form':form})

def registro(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {"mensaje":"Usuario Creado"})
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro.html", {"form":form})
    
    else:
        form = UserRegisterForm()
    
        return render(request, "registro.html", {"form":form})

@login_required(login_url="Login")
def editar_perfil(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            
            usuario.save()
            
            return render(request, "inicio.html", {"mensaje": "Datos actualizados"})
        
        return render(request, "perfil.html", {"mensaje":"Contraseñas no coinciden"})
    
    else:
        
        form = UserEditForm(instance=request.user)
        
        return render(request, "perfil.html", {"form":form})

def catalogo(request):
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'tienda.html', {'categorias': categorias, 'productos':productos})

def buscar(request):
    
    if request.GET['nombre']:
        
        nombre = request.GET['nombre']
        
        productos = Producto.objects.filter(nombre__icontains=nombre)
        
        return render(request, 'busqueda.html', {'productos':productos, 'nombre':nombre})   
    
    else:
        
        respuesta = 'No se encontró ese producto'
        
        return render(request, 'busqueda.html', {"respuesta":respuesta})

@login_required(login_url="Login")
def contacto(request):
    
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            servicio = form.cleaned_data['servicio']
            mensaje = form.cleaned_data['mensaje']
            
            # Envío del correo electrónico
            
            asunto = 'Nuevo mensaje de contacto'
            mensaje = f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'
            correo_origen = settings.EMAIL_HOST_USER
            correo_destino = ['nahuel.nogueira93@hotmail.com']
            
            send_mail(asunto, mensaje, correo_origen, correo_destino, fail_silently=False)
            
            return render(request, 'confirmacion.html')
        
    else:
        
        form = ContactForm()
        
    return render(request, 'contacto.html', {'form': form})

def confirmacion(request):
    return render(request, 'confirmacion.html')

@login_required(login_url="Login")
def servicios(request):
    
    servicios = Servicios.objects.all()
    
    return render(request, 'servicios.html', {"servicios":servicios})

def nosotros(request):
    
    return render(request, 'nosotros.html')