
from django.contrib.auth.models import Group
from rest_framework import generics

from ..models import MenuItem
from ..permissions import IsManager
from ..serializers import MenuItemSerializer


class MenuItemCreate(generics.CreateAPIView):
    permission_classes = [IsManager]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
