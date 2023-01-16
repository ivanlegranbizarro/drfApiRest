from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:pk>/', views.CategoriaDetailAndCreateView.as_view()),
    path('articulos/', views.ArticuloView.as_view()),
    path('articulos/<int:pk>/', views.ArticuloDetailAndCreateView.as_view())
]
