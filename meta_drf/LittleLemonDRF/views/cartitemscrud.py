from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from ..models import Cart, OrderItem
from ..serializers import UpdateOrderItemSerializer

class CartItemDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateOrderItemSerializer
    queryset = Cart.objects.all()
    lookup_url_kwarg = 'pk'

    def get_object(self):
        if self.request.user.is_authenticated:
            order_id = self.kwargs["pk"]
            cart_item = get_object_or_404(OrderItem, id=order_id, user=self.request.user)
            return cart_item

    def delete(self, request, pk=None):
        content = self.get_object()
        print(content)
        content.delete()
        return JsonResponse({'Data': "Item deleted sucessfully"}, safe=False)

