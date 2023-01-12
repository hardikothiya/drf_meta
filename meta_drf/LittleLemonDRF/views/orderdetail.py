from django.http import  Http404
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from ..models import Order
from ..serializers import OrderListSerializer


class OrderDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer

    def get_object(self):
        try:
            return Order.objects.get(id=self.kwargs.get('pk'), )
        except Order.DoesNotExist:
            raise Http404
