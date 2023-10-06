from rest_framework import serializers
from .models import Product, DeliveryAdress, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class DeliveryAdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAdress
        fields = "__all__"


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = "__all__"
