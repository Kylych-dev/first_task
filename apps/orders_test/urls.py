from django.urls import include, path
from rest_framework import routers
from .app_module.views import OrderAPIView, InvoiceAPIView

order_router = routers.DefaultRouter()
order_router.register(r'orders', OrderAPIView)

invoice_router = routers.DefaultRouter()
invoice_router.register(r'invoice', InvoiceAPIView)

urlpatterns = [
    path('order', include(order_router.urls)),
    path('invoice', include(invoice_router.urls))
]
