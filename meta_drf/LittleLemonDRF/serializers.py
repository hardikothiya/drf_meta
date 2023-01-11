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
        fields = ['user', 'quantity', 'price', 'menuitem', 'cart']
        read_only_fields = ('price', 'cart')

        def create(self, validated_data):
            return OrderItem(**validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    menu_i = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = "__all__"

    def get_menu_i(self, obj):
        print(obj.id)
        items_obj = OrderItem.objects.filter(user=obj.user).values()

        # cart = Cart.objects.create(user=obj.user)
        # cart.save()

        return list(items_obj)

    # create a new cart for the user


class OrderListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self, obj):
        items_obj = OrderItem.objects.filter(user=obj.user).values()
        return list(items_obj)


class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.is_delivered = validated_data.get('is_delivered', instance.email)
    #     instance.save()
    #     return instance





