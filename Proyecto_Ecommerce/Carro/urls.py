from . import views
from django.urls import path

app_name="Carro"

urlpatterns = [
    path("carrito/", views.carrito, name="Carrito"),
    path("agregar/<int:producto_id>", views.agregar_producto, name="Agregar"),
    path("eliminar/<int:producto_id>", views.eliminar_producto, name="Eliminar"),
    path("restar/<int:producto_id>", views.restar_producto, name="Restar"),
    path("limpiar/", views.limpiar_carro, name="Limpiar"),
]