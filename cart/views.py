from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class AddToCart(APIView):

    def post(self, request):
        data = request.data
        cart = Cart(request)
        cart.add(
            product=data.get('product'),
            quantity=data.get('quantity'),
            update_quantity=data.get('update_quantity')
        )
        return Response({"details": "Item added successfully to cart"}, status=status.HTTP_200_OK)


class RemoveFromCart(APIView):

    def post(self, request):
        data = request.data
        cart = Cart(request)
        cart.remove(data.get('product'))
        return Response({"details": "Item removed from cart successfully"}, status=status.HTTP_200_OK)


class CartDetailView(APIView):

    def get(self, request):
        cart = Cart(request)
        return Response(cart, status=status.HTTP_200_OK)
