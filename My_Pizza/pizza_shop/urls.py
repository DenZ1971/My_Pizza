from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductViewSet, DeliveryAdressViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename="product")
router.register('delivery_adress', DeliveryAdressViewSet, basename="delivery_adress")

urlpatterns = router.urls


# urlpatterns = [
#     path("product/", ProductViewSet.as_view({'get': 'list'})),
#     path("product/<int:pk>", ProductViewSet.as_view({'get': 'retrieve'})),
#     path("product/create/", ProductViewSet.as_view({'post': 'create'})),
#     path("product/<int:pk>/update/", ProductViewSet.as_view({'put': 'update'}))
#
#
# ]