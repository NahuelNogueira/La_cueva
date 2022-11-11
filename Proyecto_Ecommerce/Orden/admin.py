from django.contrib import admin
from .models import Pedido, Item_Pedido

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Item_Pedido)