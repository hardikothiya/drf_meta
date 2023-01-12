
from rest_framework import serializers

from ..models import Order

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'cart']
        extra_kwargs = {"user": {"required": False, "allow_null": True}}
