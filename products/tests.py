from django.test import TestCase
from .models import Product
from mixer.backend.django import mixer
import pytest
from hypothesis import strategies as st, given
pytest_mark = pytest.mark.django_db


# Create your tests here.

class TestProductModel:

    def setUp(self) -> None:
       product = mixer.blend(Product, name="product_name")

    def test_product_was_created(self):
        product = mixer.blend(Product, name="product_name")
        assert product.name == "product_name"

    def test_str_return(self):
        product = mixer.blend(Product, name="product_name")
        product_result = Product.objects.last()
        assert str(product_result) == "product_name"

    @given(st.characters)
    def test_product_name(self, name):
        print(name, "name st")
        product = mixer.blend(Product, name=name)
        product_result = Product.objects.last()
        assert product.name == str(name)
