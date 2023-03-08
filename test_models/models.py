from django.db import models


# Таблица "Пользователи"
class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилиия пользователя')
    user_email = models.CharField(max_length=100, verbose_name='Электронная почта')
    user_password = models.CharField(max_length=100, verbose_name='Пароль')
    delivery_address = models.CharField(max_length=100, verbose_name='адрес доставки')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.first_name

# Таблица "Товары"
class Product(models.Model):
    product_title = models.CharField(max_length=100, verbose_name='Наименование товара')
    category = models.CharField(max_length=100, verbose_name='Категория')
    product_description = models.CharField(max_length=100, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity_stock = models.PositiveIntegerField(verbose_name = 'Количество на складе')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
    
# Таблица "Заказы"
class Orders(models.Model):
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


#  Авторизация JWT

