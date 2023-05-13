from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.decorators import login_required
from .models import Pedido, Item_Pedido
from Carro.carro import Carro
from Tienda.views import confirmacion
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="Login")
def procesar_pedido(request):
    
    pedido = Pedido.objects.create(user=request.user)
    
    carro = Carro(request)
    
    items=list()
    
    for key, value in carro.carro.items():
        
        items.append(Item_Pedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
        
    Item_Pedido.objects.bulk_create(items)
    
    asunto = "Nuevo pedido"
    mensaje = f'Nombre: {request.user}\n\nProductos:\n{items}'
    
    from_email=settings.EMAIL_HOST_USER
    
    send_mail(asunto, mensaje, from_email, ['nahuel.nogueira93@hotmail.com'], fail_silently=False)
    
    return confirmacion(request)