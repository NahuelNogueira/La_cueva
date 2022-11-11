from django.db import models
from Producto.models import Producto
from django.contrib.auth.models import User

# Create your models here.

class Item_Pedido(models.Model):
    
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='item', on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"
    

class Pedido(models.Model):
    
    PEDIDO = 'pedido'
    ENVIADO = 'enviado'
    
    ESTADOS = (
        (PEDIDO, 'Pedido'),
        (ENVIADO , 'Enviado')
    )
    
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Item_Pedido)
    fecha_pedido = models.DateField(auto_now_add=True)
    pagado = models.BooleanField()
    precio_compra = models.IntegerField()
    estado = models.CharField(max_length=50, choices=ESTADOS, default=PEDIDO)
    