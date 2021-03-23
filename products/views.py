from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Category, Product, Photo
from .serializers import CategorySerializer, ProductReadSerializer, PhotoSerializer


# Create your views here.

class CategoryCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    lookup_field = "id"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductReadSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductUpdateView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer


class ProductDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer


class PhotoCreateView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoListView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)


class PhotoUpdateView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
