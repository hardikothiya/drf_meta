

from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from ..models import Cart
from ..serializers import CartItemSerializer
class CartItems(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(is_active=True, user=self.request.user)
        return Cart.objects.none()