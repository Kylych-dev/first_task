from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import UserSerializer, RegistratorSerializer
from rest_framework.permissions import AllowAny


class UserAPIView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

    
class RegistratorSerializer(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistratorSerializer