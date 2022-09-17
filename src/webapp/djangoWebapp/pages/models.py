from django.db import models
from time import time
from django.utils import timezone

from django.db.models.fields import DateTimeField


# Sensor Data
class SensorData(models.Model):
    heart_rate = models.FloatField(default=0.0)
    body_temp = models.FloatField(default=0.0)
    date = DateTimeField(default=timezone.now)
    ts = models.IntegerField(default=int(time()))

    def __str__(self):
        r = f'Date: {self.date} heart_rate: {self.heart_rate} - body_temp: {self.body_temp}'
        return r
