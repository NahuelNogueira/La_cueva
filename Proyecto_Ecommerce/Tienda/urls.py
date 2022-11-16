from django.contrib.auth import views
from django.urls import path

from .views import inicio, catalogo,  login, signup

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('catalogo', catalogo, name='Catalogo'),
    path('login', login, name='Login'),
    path('signup', signup, name='Signup'),
]