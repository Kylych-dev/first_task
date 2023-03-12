from django.contrib import admin
from .api.models import Orders, Invoice


admin.site.register(Orders)
admin.site.register(Invoice)
