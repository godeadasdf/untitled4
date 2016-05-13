from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=20)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'Item'
