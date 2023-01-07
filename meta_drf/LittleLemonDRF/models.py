from django.db import models

from django.contrib.auth.models import User


class Categorey(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True, default=False)
    categorey = models.ForeignKey(Categorey, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('menuitem', 'user')

    def __str__(self):
        return str(self.user)

    def get_price(self):
        result = self.unit_price * self.quantity
        return result

    def save(self, *args, **kwargs):
        self.price = self.get_price()
        super(Cart, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def __str__(self):
        return str(self.user)


class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('order', 'menuitem')

    def __str__(self):
        return str(self.order)

    def get_price(self):
        result = self.unit_price * self.quantity
        return result

    def save(self, *args, **kwargs):
        self.price = self.get_price()
        super(OrderItem, self).save(*args, **kwargs)
