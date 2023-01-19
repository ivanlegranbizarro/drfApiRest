from django.test import TestCase
from .models import Articulo

# Create your tests here.

class BlogTests(TestCase):
  def test_post_str(self):
    articulo = Articulo(nombre='A sample title')
    self.assertEqual(str(articulo), articulo.nombre)


