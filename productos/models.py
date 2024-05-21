from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    # Cadena de texto limitada en caracteres
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # Relacionamos producto con categoria
    # creamos la referencia a otra clase
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
