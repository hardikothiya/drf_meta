from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Order
from ..serializers import OrderListSerializer


class OrderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_delivered']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()
