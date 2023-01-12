from .serializers import *
from django.contrib.auth.models import User, Group
from .models import MenuItem, Cart, OrderItem, Order
from django.http import JsonResponse, Http404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from django.shortcuts import get_object_or_404

from .permissions import IsManager
from django.contrib.auth.models import Group


class UserList(generics.ListCreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs.get('pk'))

        except User.DoesNotExist:

            raise Http404


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


class MenuListModify(generics.RetrieveUpdateDestroyAPIView):
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
            return Cart.objects.filter(is_active=True, user=self.request.user)
        return Cart.objects.none()


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


class OrderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_delivered']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()


class OrderDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer

    def get_object(self):
        try:
            return Order.objects.get(id=self.kwargs.get('pk'), )
        except Order.DoesNotExist:
            raise Http404



class CreateOrderItem(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=self.request.user, is_active=True)
        #
        except Exception as e:
            cart = Cart.objects.create(user=self.request.user, is_active=True)
        manager_group = User.objects.get(username=self.request.user)
        serializer_data = self.request.data
        serializer_data['user'] = manager_group.id
        serializer_data['cart'] = cart.id
        try:
            dataa = OrderItemSerializer(data=serializer_data)
            if dataa.is_valid():
                dataa.save()
                return JsonResponse(dataa.data)

            else:
                return JsonResponse(dataa.errors)
        except Exception as e:
            return JsonResponse({"data": "No detaails Found"}, safe=False)


class PlaceOrder(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaceOrderSerializer

    def perform_create(self, request):
        manager_group = User.objects.get(username=self.request.user)
        serializer_data = self.request.data
        serializer_data['user'] = manager_group.id

        try:
            cart = Cart.objects.get(user=manager_group.id, is_active=True)
            print(cart)
            serializer_data['cart'] = cart.id
            print(cart.id)
            dataa = PlaceOrderSerializer(data=serializer_data)
            print(dataa)
            if dataa.is_valid():
                print('==========')
                dataa.save()
                print("--")
                cart.is_active = False
                cart.save()
                return JsonResponse(dataa.data)
            else:
                return JsonResponse(dataa.errors)
        except Exception as e:
            print('sssssssssss')
            raise Http404

class MenuListModify(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]

    serializer_class = MenuItemSerializer
    lookup_url_kwarg = 'pk'
    queryset = MenuItem.objects.all()

    def delete(self, request, pk=None):
        content = self.get_object()
        content.delete()
        return JsonResponse('return some info', safe=False)
class OrderDeliverBy(generics.RetrieveUpdateAPIView):
    permission_classes = [IsManager]
    serializer_class = UpdateOrderSerializer
    lookup_url_kwarg = 'pk'

    def get_object(self):
        order_id = self.kwargs["pk"]
        order = get_object_or_404(Order, id=order_id)
        print(order)
        return get_object_or_404(Order, id=order_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
