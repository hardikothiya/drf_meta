from rest_framework import serializers

from ..models import OrderItem

class UpdateOrderItemSerializer(serializers.ModelSerializer):
    # cart = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['user', 'quantity']
        extra_kwargs = {"user": {"required": False, "allow_null": True}}
