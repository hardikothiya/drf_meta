# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from rest_framework import serializers
# from .models import MenuItem, Cart, Order, OrderItem
# from django.contrib.auth.models import Group
#
#
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'name')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'id']
#
#     def create(self, validated_data):
#         userdata = User.objects.create_user(**validated_data)
#         user = User.objects.get(username=userdata.username)
#         Cart.objects.create(user=user)
#         return userdata
#
#
# class MenuItemSerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='categorey.title')
#
#     class Meta:
#         model = MenuItem
#
#         fields = ['title', 'price', 'category_name']
#
#
# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ['user', 'quantity', 'menuitem', 'cart']
#         extra_kwargs = {"user": {"required": False, "allow_null": True},
#                         }
#
#
#
#
#     # def update(self, instance, validated_data):
#     #     instance.quantity = validated_data.get('quantity', instance.quantity)
#     #     print(instance.quantity)
#     #     instance.user = validated_data.get('user', instance.user)
#     #     instance.save()
#     #     return instance
#
#
# class UpdateOrderItemSerializer(serializers.ModelSerializer):
#     # cart = serializers.SerializerMethodField()
#
#     class Meta:
#         model = OrderItem
#         fields = ['user', 'quantity']
#         extra_kwargs = {"user": {"required": False, "allow_null": True}}
#
#
# class CartItemSerializer(serializers.ModelSerializer):
#     menu_i = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Cart
#
#         fields = "__all__"
#         extra_kwargs = {"user": {"required": False, "allow_null": True}}
#
#     def get_menu_i(self, obj):
#         print(obj)
#         items_obj = OrderItem.objects.filter(user=obj.user, cart_id=obj.id).values()
#         return list(items_obj)
#
#
# class OrderListSerializer(serializers.ModelSerializer):
#     items = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#
#     def get_items(self, obj):
#         items_obj = OrderItem.objects.filter(user=obj.user).values()
#         return list(items_obj)
#
#
# class PlaceOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['user', 'cart']
#         extra_kwargs = {"user": {"required": False, "allow_null": True}}
#
#
# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['is_delivered', 'delivery_crew', 'user']
#         extra_kwargs = {"user": {"required": False, "allow_null": True}}
#
#     def update(self, instance, validated_data):
#         instance.is_delivered = validated_data.get('is_delivered', instance.is_delivered)
#         instance.delivery_crew = validated_data.get('delivery_crew', instance.delivery_crew)
#         instance.user = validated_data.get('user', instance.user)
#         instance.save()
#         return instance
