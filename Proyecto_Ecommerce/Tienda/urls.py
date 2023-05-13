from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('catalogo', catalogo, name='Catalogo'),
    path('login', login_request, name='Login'),
    path('registro', registro, name='Registro'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar_perfil', editar_perfil, name='Perfil'),
    path('buscar', buscar, name='Buscar'),
    path('contacto', contacto, name='Contacto'),
    path('confirmacion', confirmacion, name='Confirmacion'),
    path('servicios', servicios, name='Servicios'),
    path('nosotros', nosotros, name='Nosotros'),
]