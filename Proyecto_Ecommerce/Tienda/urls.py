from django.contrib.auth import views
from django.urls import path

from .views import inicio, catalogo

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('catalogo', catalogo, name='Catalogo'),
]