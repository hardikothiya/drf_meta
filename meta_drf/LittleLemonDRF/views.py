from django.shortcuts import render
from .serializers import UserSerializer, MenuItemSerializer, GroupSerializer, CartItemSerializer, OrderListSerializer
from django.contrib.auth.models import User, Group
from .models import MenuItem, Cart, OrderItem, Order
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .permissions import IsManager
from django.contrib.auth.models import Group


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


class ManagerList(generics.ListAPIView):
    permission_classes = []

    queryset = Group.objects.filter(name='managers')
    serializer_class = GroupSerializer


class ManagerRole(generics.CreateAPIView):
    permission_classes = []
    serializer_class = GroupSerializer

    def perform_create(self, request):
        id = request.data
        queryset = User.objects.get(name=id['name'])
        print(queryset)

        user = GroupSerializer(queryset)
        if user.is_valid():
            manager_group = Group.objects.get(name='manager')
            manager_group.user_set.add(user)
            manager_group.save()
            return JsonResponse("hhhh", safe=False)


class CartItems(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            print(self.request.user)
            return Cart.objects.filter(user=self.request.user)
        return Cart.objects.none()


class CartItemDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    queryset = Cart.objects.all()
    lookup_url_kwarg = 'pk'
    queryset = MenuItem.objects.all()

    def delete(self, request, pk=None):
        content = self.get_object()
        content.delete()
        return JsonResponse('return some info', safe=False)


class OrderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()

