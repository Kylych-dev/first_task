from django.core.validators import FileExtensionValidator
from django.db import models
from uuid import uuid4
from apps.product_test.base.service import get_path_upload_image as upload_image
from apps.product_test.base.service import validate_size_image as size_image


bn = dict(blank=True, null=True)
uuid = dict(primary_key=True, default=uuid4, editable=False)

class Product(models.Model):
    id                  = models.UUIDField(**uuid)
    product_title       = models.CharField(max_length=100, verbose_name='Наименование товара')
    category            = models.CharField(max_length=100, verbose_name='Категория')
    product_description = models.CharField(max_length=100, verbose_name='Описание товара')
    price               = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity_stock      = models.PositiveIntegerField(verbose_name='Количество на складе')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['product_title']
    
    def __str__(self):
        return self.product_title
    

class ImageProduct(models.Model):
    id                  = models.UUIDField(**uuid)
    picture             = models.ImageField(upload_to=upload_image,
                                            **bn,
                                            validators=[FileExtensionValidator(allowed_extensions=['jpg']),
                                                        size_image])
    product             = models.ForeignKey(Product, 
                                            on_delete=models.CASCADE, 
                                            verbose_name='Продукт', 
                                            related_name='images')
    

    class Meta: 
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    
    def __str__(self) -> str:
        return self.picture.url