from django.shortcuts import render
from Producto.models import Producto, Categoria

# Create your views here.

def inicio(request):
    
    productos = Producto.objects.all()
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def catalogo(request):
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'catalogo.html', {'categorias': categorias, 'productos':productos})