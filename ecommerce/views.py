from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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
from .permissions import IsStaffOrReadOnly, IsOwner


class ItemMVS(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsStaffOrReadOnly,]
    lookup_field = "slug"


class OrderItemMVS(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    # permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(user=user)
    
    def get_permissions(self):
        if self.request.user.is_staff:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]


class OrderMVS(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class AddressMVS(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsOwner]
