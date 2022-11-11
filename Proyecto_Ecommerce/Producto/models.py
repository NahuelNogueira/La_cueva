from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen =models.ImageField(upload_to='', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.nombre
    
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    