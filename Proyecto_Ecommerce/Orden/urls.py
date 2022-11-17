from . import views
from django.urls import path


urlpatterns = [
    path('', views.procesar_pedido, name="Procesar_pedido"),
]