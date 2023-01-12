from django.http import JsonResponse
from rest_framework import generics

from ..models import MenuItem
from ..permissions import IsManager
from ..serializers import MenuItemSerializer


class MenuListModify(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]

    serializer_class = MenuItemSerializer
    lookup_url_kwarg = 'pk'
    queryset = MenuItem.objects.all()

    def delete(self, request, pk=None):
        content = self.get_object()
        content.delete()
        return JsonResponse('return some info', safe=False)