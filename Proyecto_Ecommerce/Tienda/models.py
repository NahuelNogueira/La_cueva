from django.db import models

# Create your models here.

class Servicios(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='media')
    
    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
    
    def __str__(self):
        return self.nombre