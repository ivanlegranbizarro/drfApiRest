from django.views import generic
from rest_framework import generics

from .models import Articulo, Categoria
from .serializers import ArticuloSerializer, CategoriaSerializer

# Create your views here.


class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    model = Categoria
    serializer_class = CategoriaSerializer


class CategoriaDetailAndCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    model = Categoria
    serializer_class = CategoriaSerializer


class ArticuloView(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    model = Articulo
    serializer_class = ArticuloSerializer


class ArticuloDetailAndCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    model = Articulo
    serializer_class = ArticuloSerializer


class ArticuloListView(generic.ListView):
    model = Articulo
    template_name = 'blog/articulo_list.html'
    context_object_name = 'articulos'
