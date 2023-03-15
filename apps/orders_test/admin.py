from django.contrib import admin
from .app_module.models import Orders, Invoice


admin.site.register(Orders)
admin.site.register(Invoice)
