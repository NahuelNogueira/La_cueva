from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import UserRegisterForm
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
                
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                
                return render(request, "inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        return render(request, "inicio.html", {"mensaje":"Error, formulario erroneo"})
    
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
        form = UserRegisterForm()
    
        return render(request, "registro.html", {"form":form})

def catalogo(request):
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'catalogo.html', {'categorias': categorias, 'productos':productos})