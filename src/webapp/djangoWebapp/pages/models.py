from email.policy import default
from pyexpat import model
from sys import maxsize
from unittest.util import _MAX_LENGTH
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
    ecg = models.TextField(default="")
    ecg_connected = models.BooleanField(default=False)

    def __str__(self):
        r = f'Date: {self.date} heart_rate: {self.heart_rate} - body_temp: {self.body_temp}'
        return r

# Raspberry PI IP Address
class Ip(models.Model):
    ip = models.CharField(default="", max_length=255)
    ts = models.IntegerField(default=int(time()))
    def __str__(self):
        r = f'IP - {self.ip}'
        return r

# Historical Data
class HistoricalData(models.Model):
    heart_rate = models.FloatField(default=0.0)
    body_temp = models.FloatField(default=0.0)
    date = DateTimeField(default=timezone.now)
    ts = models.IntegerField(default=int(time()))
    patient_id = models.IntegerField(default=0)

    def __str__(self):
        r = f'PK: {self.pk} - Patient ID: {self.patient_id} Date: {self.date} heart_rate: {self.heart_rate} - body_temp: {self.body_temp}'
        return r
