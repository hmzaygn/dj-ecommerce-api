from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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
from .permissions import IsStaffOrReadOnly


class ItemMVS(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsStaffOrReadOnly,]
    lookup_field = "slug"


class OrderItemMVS(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return OrderItem.objects.all()
        
        return OrderItem.objects.filter(user=user)


class OrderMVS(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        
        return Order.objects.filter(user=user)


class AddressMVS(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Address.objects.all()
        
        return Address.objects.filter(user=user)
