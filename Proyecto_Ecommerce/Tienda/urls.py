from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import inicio, catalogo, login_request, registro


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('catalogo', catalogo, name='Catalogo'),
    path('login', login_request, name='Login'),
    path('registro', registro, name='Registro'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
]