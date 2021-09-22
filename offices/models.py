from django.db import models
from django.contrib.auth import get_user_model
from utils import Z1, Z2, Z3, Z4
from utils import P, K, R
from utils import F1, F2

AuthUserModel = get_user_model()


class Floor(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    floor_levels = models.CharField(choices=((F1, 'F1'), (F2, 'F2')),max_length=2)

    def __str__(self):
        return f'<Floor object ID = {self.id}>'


class Zone(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    floor = models.ManyToManyField(Floor)
    zone_equipment = models.CharField(choices=((P, 'P'), (K, 'K'), (R, 'R')), max_length=1)
    zone_location = models.CharField(choices=((Z1, 'Z1'), (Z2, 'Z2'), (Z3, 'Z3'), (Z4, 'Z4')), max_length=2)

    def __str__(self):
        return f'<Zone object ID = {self.id}>'


class Office(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    zone = models.ManyToManyField(Zone)
    # office_location = models.IntegerField(choices=[(x, str(x)) for x in range(1, 48)])
    # owner = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'<Office object ID = {self.id}>'
