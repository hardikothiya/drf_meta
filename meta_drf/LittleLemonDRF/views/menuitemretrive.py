from rest_framework import generics

from ..models import MenuItem
from ..serializers import MenuItemSerializer


class MenuItemRetrive(generics.RetrieveAPIView):
    def get_object(self, queryset=None):
        item_id = self.kwargs.get('pk')
        obj = MenuItem.objects.get(id=item_id)
        return obj

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
