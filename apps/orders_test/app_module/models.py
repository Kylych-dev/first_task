from django.db import models
from uuid import uuid4
from apps.user_test.app_module.models import Account
from apps.product_test.app_module.models import Product

# param = dict(null=True, blank=True)

class Orders(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id         = models.ForeignKey(Account, 
                                        on_delete=models.CASCADE, 
                                        verbose_name='id пользователя',
                                        related_name='users_order')
    order_date      = models.DateTimeField(verbose_name='Дата и время заказа товара')
    order_price     = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма заказа')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.user_id
    

class Invoice(models.Model):
    order_id        = models.ForeignKey(Orders, 
                                        on_delete=models.CASCADE, 
                                        verbose_name='id заказа',
                                        related_name='order_invoices')
    product_id      = models.ForeignKey(Product, 
                                        on_delete=models.CASCADE, 
                                        verbose_name='id товара',
                                        related_name='product_invoices')
    number_goods    = models.PositiveIntegerField(verbose_name='Количество товаров')


    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
    
    def __str__(self):
        return f'order: {self.order_id}; product:{self.product_id}'