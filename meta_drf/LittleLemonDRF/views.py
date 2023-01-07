from django.shortcuts import render
from .serializers import UserSerializer, MenuItemSerializer
from django.contrib.auth.models import User
from .models import MenuItem

from rest_framework import generics


class UserList(generics.ListCreateAPIView):
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
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListMoify(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    lookup_url_kwarg = 'pk'
    queryset = MenuItem.objects.all()



    
    
    
    