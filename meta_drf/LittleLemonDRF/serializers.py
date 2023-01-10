from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers
from .models import MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='categorey.title')

    class Meta:
        model = MenuItem

        fields = ['title', 'price', 'category_name']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menuitem']


class CartItemSerializer(serializers.ModelSerializer):
    menu_i = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = "__all__"
    def get_menu_i(self, obj):
        print(obj.id)
        items_obj = OrderItem.objects.filter(user=obj.user).values()
        return list(items_obj)


class OrderListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            "status",
            "total_price",
            'items',
        ]

    def get_items(self, obj):
        items_obj = OrderItem.objects.filter(user=obj.user).values()
        return list(items_obj)
