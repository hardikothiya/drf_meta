from rest_framework import serializers

from ..models import Order

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['is_delivered', 'delivery_crew', 'user']
        extra_kwargs = {"user": {"required": False, "allow_null": True}}

    def update(self, instance, validated_data):
        instance.is_delivered = validated_data.get('is_delivered', instance.is_delivered)
        instance.delivery_crew = validated_data.get('delivery_crew', instance.delivery_crew)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
