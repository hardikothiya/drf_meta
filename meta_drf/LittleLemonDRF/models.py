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
    price = models.FloatField(default=0)
    featured = models.BooleanField(db_index=True, default=False)
    categorey = models.ForeignKey(Categorey, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return str(self.title)

    def __int__(self):
        return self.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    total_items = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user) + "  " + str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def update_total(self):
        try:
            items = self.cartitem_set.all()
            total_price = sum([item.price for item in items])
            total_items = sum([item.quantity for item in items])
            self.total_price = total_price
            self.total_items = total_items
            self.save()
        except Exception as e:
            pass


class OrderItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem_set')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.FloatField(default=0)
    unit_price = models.FloatField(default=0)

    class Meta:
        unique_together = ('cart', 'menuitem')

    def __str__(self):
        return str(self.menuitem.title) + str(self.user.username)

    def get_price(self):
        result = self.menuitem.price * self.quantity
        return float(result)

    def save(self, *args, **kwargs):
        self.unit_price = self.menuitem.price
        print(self.menuitem.price)# optional
        self.price = self.get_price()
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
        self.cart.save()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_crew', null=True)
    total_price = models.FloatField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    total_items = models.IntegerField(null=True,blank=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        try:
            self.total_price = self.cart.total_price
            self.total_items = self.cart.total_items
            super().save(*args, **kwargs)
        except Exception as e:
            print(e)


