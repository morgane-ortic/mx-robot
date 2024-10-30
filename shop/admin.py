from django.contrib import admin
from .models import Product, Customer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock')
    search_fields = ('name', 'description', 'category')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)