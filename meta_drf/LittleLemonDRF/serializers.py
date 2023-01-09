from django.contrib.auth.models import User
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


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    menu_i = serializers.ReadOnlyField(source='menuitem.title')

    class Meta:
        model = Cart

        fields = ['quantity', 'price', 'user', 'id', 'menu_i']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
                  'id',
                  "status",
                  "total_price",
                  'items',
                  'all_items'
                  ]
        depth = 1
