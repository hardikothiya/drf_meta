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
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_items = models.IntegerField(default=2)

    def __str__(self):
        return str(self.user)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

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
        super(OrderItem, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=22)
    all_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, blank=True, null=True, related_name='all_items')
    aa_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_data', null=True, blank=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    # def get_total_price(self):
    #     return sum(item.get_price() for item in self.all_items.get_price())
    #
    # def save(self, *args, **kwargs):
    #     self.total_price = self.get_total_price()
    #     super(Order, self).save(*args, **kwargs)
