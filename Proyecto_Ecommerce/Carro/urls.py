from django.contrib.auth import views
from django.urls import path

from .views import carro


urlpatterns = [
    path('carro', carro, name='Carro')
]