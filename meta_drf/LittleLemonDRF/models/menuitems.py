from django.contrib.auth.models import User
from django.db import models

from ..models import Categorey

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.FloatField(default=0)
    featured = models.BooleanField(db_index=True, default=False)
    categorey = models.ForeignKey(Categorey, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return str(self.title)

    def __int__(self):
        return self.price
