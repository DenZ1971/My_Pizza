from rest_framework import viewsets

from .models import Product, DeliveryAdress
from .serializers import ProductSerializer, DeliveryAdressSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeliveryAdressViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryAdressSerializer
    queryset = DeliveryAdress.objects.all()
