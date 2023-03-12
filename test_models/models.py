from django.db import models
from django.urls import reverse
from uuid import uuid4


# Таблица "Пользователи"
class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилиия пользователя')
    user_email = models.CharField(max_length=100, verbose_name='Электронная почта')
    user_password = models.CharField(max_length=100, verbose_name='Пароль')
    delivery_address = models.CharField(max_length=100, verbose_name='адрес доставки')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    
    # для отображения таблицы в административной панели
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    # поменять название в ORM objects(1) на first name
    def __str__(self):
        return self.first_name
    
    # для перехода на сайт с административной панели
    '''
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    '''

# Таблица "Товары"
class Product(models.Model):
    id_products = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_title = models.CharField(max_length=100, verbose_name='Наименование товара')
    category = models.CharField(max_length=100, verbose_name='Категория')
    product_description = models.CharField(max_length=100, verbose_name='Описание товара')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity_stock = models.PositiveIntegerField(verbose_name = 'Количество на складе')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-time_create', 'product_title']

    def __str__(self):
        return self.title
    
# Таблица "Заказы"
class Orders(models.Model):
    id_order = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя')
    order_date = models.DateTimeField(verbose_name='Дата и время заказа товара')
    order_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.user_id

# Таблица "Товары в заказах"
class Invoice(models.Model):
    id_orders = models.ForeignKey(Orders, on_delete =models.CASCADE, verbose_name='id заказа')
    id_product = models.ForeignKey(Product, on_delete =models.CASCADE, verbose_name='id товара')
    number_goods= models.PositiveIntegerField(verbose_name='Количество товаров')

    class Meta: 
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'




