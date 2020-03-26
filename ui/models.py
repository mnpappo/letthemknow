from django.db import models
from .tuple_and_dictionaries import *


class Position(models.Model):
    user_id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_LIST, blank=True, null=True)
    division = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)


class Stat(models.Model):
    world_result = models.CharField(max_length=150, null=True, blank=True)
    bangladesh_result = models.CharField(max_length=300, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True)
