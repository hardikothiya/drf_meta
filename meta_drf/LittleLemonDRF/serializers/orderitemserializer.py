from rest_framework import serializers

from ..models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['user', 'quantity', 'menuitem', 'cart']
        extra_kwargs = {"user": {"required": False, "allow_null": True},
                        }

    # def update(self, instance, validated_data):
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     print(instance.quantity)
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.save()
    #     return instance
