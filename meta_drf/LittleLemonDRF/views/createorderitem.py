from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from ..models import Cart
from ..serializers import OrderItemSerializer
class CreateOrderItem(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=self.request.user, is_active=True)
        #
        except Exception as e:
            cart = Cart.objects.create(user=self.request.user, is_active=True)
        manager_group = User.objects.get(username=self.request.user)
        serializer_data = self.request.data
        serializer_data['user'] = manager_group.id
        serializer_data['cart'] = cart.id
        try:
            dataa = OrderItemSerializer(data=serializer_data)
            if dataa.is_valid():
                dataa.save()
                return JsonResponse(dataa.data)

            else:
                return JsonResponse(dataa.errors)
        except Exception as e:
            return JsonResponse({"data": "No detaails Found"}, safe=False)
