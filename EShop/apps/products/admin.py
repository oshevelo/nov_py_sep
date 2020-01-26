from django.contrib import admin
from .models import Product, Set


admin.site.register(
    Product,
    list_display=('id', 'name', 'price', 'scu', 'gtin', 'stock', 'is_available'),
    list_filter=('is_available',)
)

admin.site.register(Set, list_display=('id', 'name', 'price'))
