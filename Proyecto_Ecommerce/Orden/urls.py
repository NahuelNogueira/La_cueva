from . import views
from django.urls import path


urlpatterns = [
    path('procesar_pedido', views.procesar_pedido, name="Procesar_pedido"),
]