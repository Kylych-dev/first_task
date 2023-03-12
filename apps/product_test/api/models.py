from django.db import models

class Product(models.Model):
    product_title       = models.CharField(max_length=100, verbose_name='Наименование товара')
    category            = models.CharField(max_length=100, verbose_name='Категория')
    product_description = models.CharField(max_length=100, verbose_name='Описание товара')
    time_create         = models.DateTimeField(auto_now_add=True)   
    time_update         = models.DateTimeField(auto_now=True)
    price               = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity_stock      = models.PositiveIntegerField(verbose_name='Количество на складе')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продкуты'
        ordering = ['-time_create', 'product_title']
    
    def __str__(self):
        return self.title
    

    