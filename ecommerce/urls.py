from rest_framework.routers import DefaultRouter 

from .views import (
    ItemMVS,
    OrderItemMVS,
    OrderMVS,
    AddressMVS,
)

router = DefaultRouter()
router.register("items",ItemMVS)
router.register("orderitems",OrderItemMVS)
router.register("orders",OrderMVS)
router.register("address",AddressMVS)


urlpatterns = []

urlpatterns += router.urls