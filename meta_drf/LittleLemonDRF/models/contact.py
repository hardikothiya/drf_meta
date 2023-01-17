from django.db import models
from django.contrib.auth.models import User


class ContactDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.BigIntegerField()
    last_name = models.CharField(max_length=25)

