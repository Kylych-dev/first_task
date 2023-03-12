from rest_framework import serializers
from .models import Orders, Invoice


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['order_data', 'order_price', 'user_id', 'order_id']



class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id_orders', 'id_product', 'number_goods']