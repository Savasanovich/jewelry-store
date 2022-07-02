from django.contrib import admin

from .models import Product,Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    exclude = ['slug']


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
