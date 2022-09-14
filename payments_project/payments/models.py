from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)


class Orders(models.Model):
    item_ids = models.ManyToManyField(Items)
