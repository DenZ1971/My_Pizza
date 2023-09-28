from rest_framework import serializers
from .models import Product, DeliveryAdress


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class DeliveryAdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAdress
        fields = "__all__"
