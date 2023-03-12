from django.db import models
from uuid import uuid4
from apps.user_test.api.models import Account
from apps.product_test.api.models import Product

class Orders(models.Model):
    id_order        = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id         = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='id пользователя')
    order_date      = models.DateTimeField(verbose_name='Дата и время заказа товара')
    order_price     = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма заказа')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.user_id
    

class Invoice(models.Model):
    id_orders       = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='id заказа')
    id_product      = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='id товара')
    number_goods    = models.PositiveIntegerField(verbose_name='Количество товаров')


    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
    
    