from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    edad = models.IntegerField(null=False)
    correo = models.EmailField(max_length=200, null=False)
    contraseña = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

