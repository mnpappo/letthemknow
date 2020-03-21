from django.db import models

STATE_LIST = (('safe', 'safe'),
              ('panicked', 'panicked'),
              ('affected', 'affected'))


class Position(models.Model):
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_LIST, default='safe', help_text='Current State')
