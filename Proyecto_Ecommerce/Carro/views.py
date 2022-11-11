from django.shortcuts import render

# Create your views here.

def carro(request):
    return render(request, 'carro.html')