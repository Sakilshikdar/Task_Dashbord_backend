from rest_framework import serializers
# from .models import Product, Category, Customer
from .models import Customer,Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user',]

        def __init__(self, *args, **kwargs):
            super(CustomerSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'quantity']

        def __init__(self, *args, **kwargs):
            super(ProductSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'quantity']

        def __init__(self, *args, **kwargs):
            super(ProductSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1



