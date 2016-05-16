from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'User'


class Item(models.Model):
    owner = models.IntegerField(default=-1)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=20)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'Item'

    def __unicode__(self):
        return self.name


class History(models.Model):
    user_id = models.IntegerField(default=-1)
    detail = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'History'

    def __unicode__(self):
        return self.detail
