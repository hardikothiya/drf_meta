from django.urls import path
from . import views

from .views import UserList, UserDetail, MenuList, MenuListMoify, MenuItemRetrive, MenuItemCreate

urlpatterns = [
    path('user', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('menu-items', MenuList.as_view() ),
    path('menu-items', MenuItemCreate.as_view() ),
    path('menu-items/<int:pk>', MenuItemRetrive.as_view() ),
    path('menu-items/<int:pk>', MenuListMoify.as_view()),   
    
]
