from django.test import TestCase
from .models import Category, Product
from mixer.backend.django import mixer
import pytest

pytest_mark = pytest.mark.django_db


# Create your tests here.
class TestProductModel(TestCase):
    def setUp(self):
        product = mixer.blend(Product, name="monique")

    def test_self_name(self):
        last_product = Product.objects.last()
        assert str(last_product) == "monique"
