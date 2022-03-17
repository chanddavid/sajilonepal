from .models import Customer, Cart, OrderPlaced, Product
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
# Register your models here.


@admin.register(Customer)
class CustomeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'city', 'provience', 'post_code']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'seling_price', 'discount_price',
                    'description', 'brand', 'category', 'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer','customer_info', 'product','product_info', 'quantity', 'status']

    def customer_info(self, obj):
        link = reverse("admin:app1_customer_change", args=[obj.customer.id])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self, obj):
            link = reverse("admin:app1_product_change", args=[obj.product.id])
            return format_html('<a href="{}">{}</a>', link, obj.product.title)
