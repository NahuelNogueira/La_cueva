from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='', blank=False, null=False)
    creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=None)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
    def __str__(self):
        return self.nombre
    
    
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self):
        return self.nombre
    
    