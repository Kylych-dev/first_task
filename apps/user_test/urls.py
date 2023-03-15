from django.urls import path, include
from rest_framework import routers
from .app_module.views import UserAPIView, RegistratorSerializer
# from rest_framework_simplejwt import 


router = routers.DefaultRouter()
router.register('userreg', UserAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistratorSerializer.as_view())
]

