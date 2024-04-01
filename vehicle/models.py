from django.db import models

from skillforge.models import BaseModel
from skillforge.utils import NullableCharField


class Vehicle(BaseModel):
    make = NullableCharField(default="Unknown")
    model = NullableCharField(default="Unknown")
    year = NullableCharField(default=None)
    drive = models.CharField(max_length=150, default="Unknown")
    cylinders = models.IntegerField(default=None, null=True)
    engine_displacement = models.CharField(max_length=150, default="Unknown")
    fuel_type = models.CharField(max_length=150, default="Unknown")
    fuel_type_1 = models.CharField(max_length=150, default="Unknown")
    transmission = models.CharField(max_length=150, default="Unknown")
    vehicle_size_class = models.CharField(max_length=150, default="Unknown")
    hundred_twenty_volt_time_to_charge = models.DecimalField(max_digits=7, decimal_places=5)
