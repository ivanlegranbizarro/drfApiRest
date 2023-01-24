from django.views import generic
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Articulo, Categoria
from .serializers import ArticuloSerializer, CategoriaSerializer

# Create your views here.


# API BACKEND
@extend_schema(tags=['categorías'])
class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    model = Categoria
    serializer_class = CategoriaSerializer


@extend_schema(tags=['categorías'])
class CategoriaDetailAndCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    model = Categoria
    serializer_class = CategoriaSerializer


@extend_schema(tags=['artículos'])
class ArticuloView(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    model = Articulo
    serializer_class = ArticuloSerializer


@extend_schema(tags=['artículos'])
class ArticuloDetailAndCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    model = Articulo
    serializer_class = ArticuloSerializer


# FRONTEND (NO HAGÁIS ESTO EN VUESTRAS CASAS. Nunca se mezclan en el mismo controlador las vistas de API y las vistas de frontend)
class ArticuloListView(generic.ListView):
    model = Articulo
    template_name = 'blog/articulo_list.html'
    context_object_name = 'articulos'


# def articulo_list(request):
#     articulos = Articulo.objects.all()
#     return render(request, 'blog/articulo_list.html', {'articulos': articulos})


class ArticuloDetailView(generic.DetailView):
    model = Articulo
    template_name = 'blog/articulo_detail.html'
    context_object_name = 'articulo'
    lookup_field = 'slug'

# def articulo_detail(request, slug):
#     articulo = Articulo.objects.get(slug=slug)
#     return render(request, 'blog/articulo_detail.html', {'articulo': articulo})
