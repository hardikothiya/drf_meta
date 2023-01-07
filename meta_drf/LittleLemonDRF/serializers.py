from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import MenuItem


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem

        fields = '__all__'

