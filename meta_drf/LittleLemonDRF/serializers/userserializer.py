from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Cart

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'id']

    def create(self, validated_data):
        userdata = User.objects.create_user(**validated_data)
        user = User.objects.get(username=userdata.username)
        Cart.objects.create(user=user)
        return userdata

