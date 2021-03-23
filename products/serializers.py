from rest_framework import serializers
from .models import Category, Product, Photo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug'
        ]


# class ProductCreateSerializer(serializers.Serializer):
#     category = serializers.HyperlinkedModelSerializer()
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     available = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.category = validated_data.get('category', instance.category)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.created = validated_data.get('available', instance.available)
#         instance.save()
#         return instance


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'id',
            'product',
            'image',
            'created',
            'updated'
        ]


class ProductReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'slug',
            'description',
            'price',
            'available',
            'created',
            'updated'
        ]
