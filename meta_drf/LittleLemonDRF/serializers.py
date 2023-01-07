from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.fields import ReadOnlyField

from .models import MenuItem, Cart
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
    class Meta:
        model = MenuItem

        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    menu_i = serializers.ReadOnlyField(source='menuitem.title')

    class Meta:
        model = Cart

        fields = ['quantity', 'price', 'user', 'id', 'menu_i']
