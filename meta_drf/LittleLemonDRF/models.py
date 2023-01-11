from datetime import datetime

from django.db import models

from django.contrib.auth.models import User
from django.http import Http404


class Categorey(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.title)


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True, default=False)
    categorey = models.ForeignKey(Categorey, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return str(self.title)

    def __int__(self):
        return self.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    total_items = models.IntegerField(default=2)
    total_cost = models.FloatField(default=3)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def update_total(self):
        try:
            items = self.cartitem_set.all()
            total_cost = sum([item.price for item in items])
            total_items = sum([item.quantity for item in items])
            self.total_cost = total_cost
            self.total_items = total_items
            self.save()
        except Exception as e:
            pass


class OrderItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem_set', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.FloatField(default=1)

    class Meta:
        unique_together = ('user', 'menuitem')

    def __str__(self):
        return str(self.menuitem.title) + str(self.user.username)

    def get_price(self):
        result = self.menuitem.price * self.quantity
        return float(result)

    def save(self, *args, **kwargs):
        self.unit_price = self.menuitem.price  # optional
        self.price = self.get_price()
        try:
            self.cart = Cart.objects.get(user=self.user, is_active=True)

        except Exception as e:
            print('--------')
            cart = Cart.objects.create(user=self.user, is_active=True)
            self.cart = cart

        super().save(*args, **kwargs)
        self.cart.update_total()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        try:
            self.cart = Cart.objects.get(user=self.user, is_active=True)

        except Exception as e:
            cart = Cart.objects.create(user=self.user, is_active=True)
            self.cart = cart
        self.cart.update_total()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_crew', null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=22)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        try:
            # self.cart = Cart.objects.get(user=self.user, is_active=True)
            # self.total_price = self.cart.total_cost
            # print(self.cart.is_active)
            # self.cart.is_active = False
            # print(self.cart.is_active)
            # self.cart.save()
            super().save(*args, **kwargs)

        except Cart.DoesNotExist as e:
            print(e)


