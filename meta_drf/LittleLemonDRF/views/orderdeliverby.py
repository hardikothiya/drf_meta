from django.shortcuts import get_object_or_404
from rest_framework import generics

from ..models import Order
from ..permissions import IsManager
from ..serializers import UpdateOrderSerializer


class OrderDeliverBy(generics.RetrieveUpdateAPIView):
    permission_classes = [IsManager]
    serializer_class = UpdateOrderSerializer
    lookup_url_kwarg = 'pk'

    def get_object(self):
        order_id = self.kwargs["pk"]
        order = get_object_or_404(Order, id=order_id)
        print(order)
        return get_object_or_404(Order, id=order_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
