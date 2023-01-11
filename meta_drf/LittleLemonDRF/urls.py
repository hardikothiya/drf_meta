from django.urls import path


from .views import *

urlpatterns = [
    path('user', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('menu-items', MenuList.as_view()),
    path('menu-item', MenuItemCreate.as_view()),
    path('menu-items/<int:pk>', MenuItemRetrive.as_view()),
    path('menu-item/<int:pk>', MenuListMoify.as_view()),
    path('groups/manager/users', ManagerList.as_view()),
    path('groups/manager/users/post', ManagerRole.as_view()),
    path('cart/cart-items', CartItems.as_view()),
    path('cart/cart-item/<int:pk>', CartItemDelete.as_view()),
    path('orders', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetails.as_view()),
    path('create-order', CreateOrderItem.as_view()),
    path('place-order', PlaceOrder.as_view()),
    path('deliver-order/<int:pk>', OrderDeliverBy.as_view()),



]
