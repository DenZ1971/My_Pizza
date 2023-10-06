
from django.contrib import admin
from pizza_shop.models import Product, Category, DeliveryAdress, Order, OrderItem, DeliveryPriceCategory



admin.site.register(Product)
admin.site.register(Category)
admin.site.register(DeliveryAdress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryPriceCategory)

