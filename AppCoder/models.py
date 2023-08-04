from django.db import models
from django.template import Template
from django.contrib.auth.models import User


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True,blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    
class Fans(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null=True, default='Sin Apellido')
    pais = models.CharField(max_length=40, null=True, default='Sin Pais')
    class Meta:
            verbose_name = "Fans"
            verbose_name_plural = "Fans"
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Pais: {self.pais}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    class Meta:
            verbose_name = "Dream Achievers"
            verbose_name_plural = "Dream Achievers"
    
class Lideres(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    pais = models.CharField(max_length=30)
    
    class Meta:
            verbose_name = "Lideres"
            verbose_name_plural = "Lideres"
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Pais: {self.pais}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    
    class Meta:
            verbose_name = "Construyentes"
            verbose_name_plural = "Construyentes"
    

    
