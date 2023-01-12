
from django.contrib.auth.models import User
from django.db import models
from ..models import Cart, MenuItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_crew', blank=True,
                                      null=True)
    total_price = models.FloatField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    total_items = models.IntegerField(null=True, blank=True, default=0)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        print(self.user)
        try:
            print("--------------")
            self.total_price = self.cart.total_price
            self.total_items = self.cart.total_items
            print('saveeeeeeeeeeeeee')
            super().save(*args, **kwargs)
        except Exception as e:
            print(e)
