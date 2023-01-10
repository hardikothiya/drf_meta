from datetime import datetime

from django.db import models

from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=2)
    total_cost = models.FloatField(default=3)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        items = self.cartitem_set.all()
        total_cost = sum([item.price for item in items])
        total_items = sum([item.quantity for item in items])
        self.total_cost = total_cost
        self.total_items = total_items
        super().save(*args, **kwargs)

    def update_total(self):
        """update total_price and total_quantity fields"""
        items = self.cartitem_set.all()
        total_cost = sum([item.price for item in items])
        total_items = sum([item.quantity for item in items])
        self.total_cost = total_cost
        self.total_items = total_items
        self.save()


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
        self.cart.update_total()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.update_total()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=22)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.total_price = self.cart.total_cost
        super().save(*args, **kwargs)
