
from django.contrib.auth.models import User
from django.db import models

from ..models import Cart, MenuItem


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

