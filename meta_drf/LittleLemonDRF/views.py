from django.shortcuts import render
from .serializers import UserSerializer, MenuItemSerializer
from django.contrib.auth.models import User, Group
from .models import MenuItem
from django.http import JsonResponse

from rest_framework import generics
from .permissions import IsManager

class UserList(generics.ListCreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    def get_object(self, queryset=None): 
        user_id = self.kwargs.get('pk')
        print(user_id)
        obj = User.objects.get(id=user_id)
        return obj
    serializer_class = UserSerializer


class MenuList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrive(generics.RetrieveAPIView):
    def get_object(self, queryset=None): 
        item_id = self.kwargs.get('pk')
        obj = MenuItem.objects.get(id=item_id)
        return obj
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    
class MenuItemCreate(generics.CreateAPIView):
    permission_classes = [IsManager]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListMoify(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]

    serializer_class = MenuItemSerializer
    lookup_url_kwarg = 'pk'
    queryset = MenuItem.objects.all()

    def delete(self, request, pk=None):
        content = self.get_object()
        content.delete()
        return JsonResponse('return some info', safe=False)

    
    