from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Pedido, Item_Pedido
from Carro.carro import Carro

# Create your views here.

@login_required(login_url="Login")
def procesar_pedido(request):
    
    pedido = Pedido.objects.create(user=request.user)
    
    carro = Carro(request)
    
    items_pedidos=list()
    
    for key, value in carro.carro.items():
        
        items_pedidos.append(Item_Pedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
        
    Item_Pedido.objects.bulk_create(items_pedidos)
    
    enviar_mail(
        pedido=pedido,
        items_pedidos=items_pedidos,
        nombre_usuario=request.user.username,
        email_usuario=request.user.usermail,
    )
    
    messages.success(request, "El pedido se ha creado con éxito")
    
    return redirect('Inicio')

def enviar_mail(**kwargs):
    
    asunto = "La Bodega Cerveza"
    mensaje = render_to_string("pedido.html", {
        "pedido":kwargs.get("pedido"),
        "items_pedidos":kwargs.get("items_pedidos"),
        "nombre_usuario":kwargs.get("nombre_usuario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    
    from_email="tiendabebidas@gmail.com"
    
    to=kwargs.get("email_usuario")
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)