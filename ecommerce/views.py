from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import (
    Item,
    OrderItem,
    Order,
    Address,
)
from .serializers import (
    ItemSerializer,
    OrderItemSerializer,
    OrderSerializer,
    AddressSerializer,
    )


class ItemMVS(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderItemMVS(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderMVS(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AddressMVS(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
