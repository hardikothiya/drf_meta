from rest_framework import serializers

from ..models import Order, OrderItem

class OrderListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self, obj):
        items_obj = OrderItem.objects.filter(user=obj.user).values()
        return list(items_obj)

