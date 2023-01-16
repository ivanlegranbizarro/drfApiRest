from django.contrib import admin

from .models import Articulo, Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Articulo)
