from django.db import models


# Create your models here.
class CartItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
