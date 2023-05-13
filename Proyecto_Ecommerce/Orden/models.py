from django.db import models
from Producto.models import Producto
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField

# Create your models here.

class Pedido(models.Model):
    
    PEDIDO = 'pedido'
    ENVIADO = 'enviado'
    
    ESTADOS = (
        (PEDIDO, 'Pedido'),
        (ENVIADO , 'Enviado')
    )
    
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    pagado = models.BooleanField(null=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default=PEDIDO)
    
    @property
    def total(self):
        return self.item_pedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )['total']
        
class Item_Pedido(models.Model):
    
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='item', on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"
    

    