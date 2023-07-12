from django.db import models
from distutils.command.upload import upload

# Create your models here.


class Periodista(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)
    rango = models.CharField(max_length=10)
    imagen = models.ImageField(
        upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.nombre, self.rango)


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
