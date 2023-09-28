
from django.contrib import admin
from pizza_shop.models import Product, Category, DeliveryAdress, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(DeliveryAdress)
admin.site.register(Order)

