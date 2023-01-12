from rest_framework import serializers
from ..models import Cart, OrderItem

class CartItemSerializer(serializers.ModelSerializer):
    menu_i = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = "__all__"
        extra_kwargs = {"user": {"required": False, "allow_null": True}}

    def get_menu_i(self, obj):
        print(obj)
        items_obj = OrderItem.objects.filter(user=obj.user, cart_id=obj.id).values()
        return list(items_obj)
