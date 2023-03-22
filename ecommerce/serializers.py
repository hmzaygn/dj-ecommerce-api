from rest_framework import serializers

from .models import (
    Item,
    OrderItem,
    Order,
    Address,
)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "title",
            "price",
            "category",
            "image",
            "description",
        )


class OrderItemSerializer(serializers.ModelSerializer):

    item = serializers.StringRelatedField()
    item_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "user",
            "user_id",
            "ordered",
            "item",
            "item_id",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)
    # item_id=serializers.IntegerField()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "items",
            # "item_id",
            "start_date",
            "shipping_date",
            "ordered",
            "address",  
            "payment"
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
           "id", 
            "user",
            "address",
            "city",
            "country",
        )