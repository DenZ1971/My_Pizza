from django.db import models
from accounts.models import User


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=520, blank=True)
    size = models.ImageField(blank=True)
    weight = models.ImageField(blank=True)
    price = models.ImageField(blank=True)
    image = models.ImageField(blank=True)


class Category(models.Model):
    category = models.CharField(max_length=128)


class DeliveryAdress(models.Model):
    customer_name = models.CharField(max_length=256)
    postcode = models.IntegerField()
    street = models.CharField(max_length=256)
    house_number = models.IntegerField()
    apt_number = models.IntegerField()
    phone_number = models.IntegerField()
    delivery_category = models.CharField(max_length=2, )


class DeliveryPriceCategory(models.Model):
    ZONE00 = '00'
    ZONE01 = '01'
    ZONE02 = '02'
    ZONE03 = '03'
    ZONE04 = '04'
    ZONE05 = '05'

    CATEGORY_CHOICES = (
        (ZONE00, 'pickup'),
        (ZONE01, 'city center'),
        (ZONE02, 'clothe to city center'),
        (ZONE02, 'far from city center'),
        (ZONE04, 'town outskirts'),
        (ZONE05, 'suburb'),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    delivery_price = models.IntegerField()


class Order(models.Model):
    CASH_ON_DELIVERY = 'CSHD'
    CARD_IN_ADVANCE = 'CRDA'

    PAYMENT_CHOICES = (
        (CASH_ON_DELIVERY, 'cash on delivery'),
        (CARD_IN_ADVANCE, 'card in advance')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_adress = models.ForeignKey(DeliveryAdress, on_delete=models.CASCADE)
    delivery_price = models.ForeignKey(DeliveryPriceCategory, on_delete=models.CASCADE)
    order_sum_price = models.IntegerField()
    payment_type = models.CharField(max_length=4, choices=PAYMENT_CHOICES)
