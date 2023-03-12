from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_title', 'category', 'product_description', 
                  'time_create', 'time_update', 'price', 'quantity_stock']