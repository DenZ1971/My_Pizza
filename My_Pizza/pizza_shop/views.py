from _decimal import Decimal

from rest_framework import viewsets, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .cart import Cart
from .models import Product, DeliveryAdress, Order, OrderItem, DeliveryPriceCategory
from .serializers import ProductSerializer, DeliveryAdressSerializer, OrderSerializer


# Create your views here.
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeliveryAdressViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryAdressSerializer

    def get_queryset(self):
        user = self.request.user
        return DeliveryAdress.objects.filter(user)


class CartAPI(APIView):
    def get(self, request, format=None):
        cart = Cart(request)

        return Response({"data": list(cart.__iter__()), "cart_total_price": cart.get_total_price()},
                        status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

        if "clean" in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(
                product=product["product"],
                quantity=product["quantity"],
                update_quantity=product["update_quantity"]
            )

        return Response({"message": "cart updated"}, status=status.HTTP_202_ACCEPTED)


#
# class CreateOrder(generics.CreateAPIView):
#     serializer = OrderSerializer
#     def create(self, request, *args, **kwargs):
#
#         cart = Cart(request)
#         user = request.user
#
#         if len(cart) == 0:
#             return Response({"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
#
#         order = Order.objects.create(customer=user)
#         delivery_adress, _ = DeliveryAdress.objects.get_o_create(user=user)
#         for item in cart:
#             order.product.add(list(cart.__iter__()))  #(item["product"], throu_defaults={"quantity": item["quantity"]})
#             order.quantity.add(item["quantity"])
#
#         delivery_price = request.data.get("delivery_price")
#         order_sum_price = cart.get_total_price() + delivery_price
#         payment_type = request.data.get("payment_type")
#         cart.clear()
#
#         serializer = OrderSerializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart(request)
        user = request.user

        delivery_adress, _ = DeliveryAdress.objects.get_or_create(
            user=user)
        delivery_price_category = DeliveryPriceCategory.objects.get(category=delivery_adress.delivery_category)
        order_sum_price = cart.get_total_price() + delivery_price_category.delivery_price
        payment_type = 'CSHD'

        order = Order.objects.create(
            customer=user,
            delivery_adress=delivery_adress,
            delivery_price=delivery_price_category,
            order_sum_price=order_sum_price,
            payment_type=payment_type,
        )

        for item in list(cart.__iter__()):
            OrderItem.objects.create(
                order=order,
                product=get_object_or_404(Product, id=item["product"]["id"]),
                quantity=item["quantity"],
                price=item['price'],
            )

        cart.clear()

        return Response(status=status.HTTP_201_CREATED)
