from django.shortcuts import render
from .models import Orders, Invoice
from .serializers import OrdersSerializer, InvoiceSerializer
from rest_framework import viewsets


class OrderAPIView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class InvoiceAPIView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


