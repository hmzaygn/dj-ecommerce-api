from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # obj = get_object_or_404(Item, id=request.data["item_id"])
        orderItem_queryset = OrderItem.objects.filter(user_id=request.user.id, item_id=request.data["item_id"])
        

        if orderItem_queryset.exists():
            data ={
                "message": "You already have this item"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            OrderItem.objects.create(user_id=request.user.id, item_id=request.data["item_id"], quantity=request.data["quantity"])
            data ={
                "message": "ADDED"
            }
            return Response(data, status=status.HTTP_201_CREATED)


        


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
