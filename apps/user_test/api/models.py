from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountMnanager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(user=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username 
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    id_user          = models.UUIDField(primary_key=True,
                                           default=uuid4,
                                           editable=False)
    first_name       = models.CharField(max_length=100, verbose_name='Имя пользователя')
    last_name        = models.CharField(max_length=100, verbose_name='Фамилиия пользователя')
    user_email       = models.CharField(max_length=200, 
                                           null=False,
                                           blank=False,
                                           verbose_name='Электронная почта')
    user_password    = models.CharField(max_length=100, verbose_name='Пароль')
    delivery_address = models.CharField(max_length=100, verbose_name='адрес доставки')
    phone_number     = models.CharField(max_length=100, verbose_name='Номер телефона')

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self) -> str:
        return self.user_email
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

