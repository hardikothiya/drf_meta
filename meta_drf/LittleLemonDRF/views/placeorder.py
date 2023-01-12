from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Cart
from ..serializers import PlaceOrderSerializer


class PlaceOrder(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaceOrderSerializer

    def perform_create(self, request):
        manager_group = User.objects.get(username=self.request.user)
        serializer_data = self.request.data
        serializer_data['user'] = manager_group.id

        try:
            cart = Cart.objects.get(user=manager_group.id, is_active=True)
            print(cart)
            serializer_data['cart'] = cart.id
            print(cart.id)
            dataa = PlaceOrderSerializer(data=serializer_data)
            print(dataa)
            if dataa.is_valid():
                print('==========')
                dataa.save()
                print("--")
                cart.is_active = False
                cart.save()
                return JsonResponse(dataa.data)
            else:
                return JsonResponse(dataa.errors)
        except Exception as e:
            print('sssssssssss')
            raise Http404
