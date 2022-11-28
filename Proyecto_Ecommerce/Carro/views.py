from django.shortcuts import render, redirect
from .carro import Carro
from Producto.models import Producto, Categoria
from django.contrib.auth.decorators import login_required

# Create your views here.

def carrito(request):
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'carrito.html', {"categorias":categorias, "productos":productos})

@login_required(login_url="Login")
def agregar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
    
    return redirect("Catalogo")

@login_required(login_url="Login")
def eliminar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    
    return redirect("Carro:Carrito")

@login_required(login_url="Login")
def restar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto=producto)
    
    return redirect("Carro:Carrito")

@login_required(login_url="Login")
def limpiar_carro(request, producto_id):
    
    carro=Carro(request)
    
    carro.limpiar_carro()
    
    return redirect("Catalogo")