from django.urls import path, include
from rest_framework import routers
from .api.views import UserAPIView

router = routers.DefaultRouter()
router.register('userreg', UserAPIView, )


urlpatterns = [
    path('product', include(router.urls))
]

