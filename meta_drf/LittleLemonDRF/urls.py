from django.urls import path

from .views import UserList, UserDetail, MenuList, MenuListMoify, MenuItemRetrive, MenuItemCreate, ManagerList, \
    ManagerRole
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
    path('cart/menu-items', CartItems.as_view()),
    path('cart/menu-item/<int:pk>', CartItemDelete.as_view()),
    path('orders', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetails.as_view()

)

]
