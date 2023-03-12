from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id_user', 'first_name', 'last_name', 'user_email')


class RegistratorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = Account
        fields = ('id_user', 'first_name', 'last_name', 'user_email', 'password', 'delivery_address', 'phone_number')

    def validate_user_email(self, value):
        '''Проверка, что электронный адрес пользователя не зарегистрирован ранее.'''
        if Account.objects.filter(user_email=value).exists():
            raise serializers.ValidationError('Пользователь с таким адресом электронной почты уже зарегистрирован.')
        return value

    def create(self, validated_data):
        '''Создание и сохранение нового пользователя.'''
        user = Account.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_email=validated_data['user_email'],
            delivery_address=validated_data['delivery_address'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

