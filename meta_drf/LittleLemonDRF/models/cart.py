from django.contrib.auth.models import User
from django.db import models


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

