from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductViewSet, DeliveryAdressViewSet, CartAPI, CreateOrder

router = DefaultRouter()
router.register('product', ProductViewSet, basename="product")
router.register('delivery_adress', DeliveryAdressViewSet, basename="delivery_adress")

urlpatterns = [path("", include(router.urls)),
               path("cart", CartAPI.as_view(), name="cart"),
               path("create_order", CreateOrder.as_view(), name="create_order")
               ]

# urlpatterns = [
#     path("product/", ProductViewSet.as_view({'get': 'list'})),
#     path("product/<int:pk>", ProductViewSet.as_view({'get': 'retrieve'})),
#     path("product/create/", ProductViewSet.as_view({'post': 'create'})),
#     path("product/<int:pk>/update/", ProductViewSet.as_view({'put': 'update'}))
#
#
# ]
