from django.contrib.auth.models import Group
from rest_framework import generics

from ..serializers import MenuItemSerializer
from ..models import  MenuItem


class MenuList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
