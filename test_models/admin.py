from django.contrib import admin
from .models import User, Orders, Invoice, Product

admin.site.register(User)
admin.site.register(Orders)
admin.site.register(Invoice)
admin.site.register(Product)