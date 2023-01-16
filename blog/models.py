from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
