from django.shortcuts import render, redirect
from .carro import Carro
from Producto.models import Producto, Categoria

# Create your views here.

def carrito(request):
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'carrito.html', {"categorias":categorias, "productos":productos})

def agregar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
    
    return redirect("Carro:Carrito")

def eliminar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    
    return redirect("Carro:Carrito")

def restar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto = Producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto=producto)
    
    return redirect("Carro:Carrito")

def limpiar_carro(request, producto_id):
    
    carro=Carro(request)
    
    carro.limpiar_carro()
    
    return redirect("Catalogo")