from django.urls import include, path
from rest_framework import routers
from .api.views import ProductAPIView

product_router = routers.DefaultRouter()
product_router.register(r'product', ProductAPIView)

urlpatterns = [
    path('product', include(product_router.urls))
]

