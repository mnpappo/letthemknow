from django.db import models

STATE_LIST = (('safe', 'safe'),
              ('panicked', 'panicked'),
              ('affected', 'affected'))

DIVISION_LIST = (('dhaka', 'Dhaka'),
                 ('chittagong', 'Chittagong'),
                 ('barisal', 'Barisal'),
                 ('khulna', 'Khulna'),
                 ('mymensingh', 'Mymensingh'),
                 ('rajshahi', 'Rajshahi'),
                 ('rangpur', 'Rangpur'),
                 ('sylhet', 'Sylhet'),
                 )


class Position(models.Model):
    user_id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_LIST, blank=True, null=True)
    division = models.CharField(max_length=50, choices=DIVISION_LIST, null=True, blank=True)
