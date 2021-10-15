from django.db import models
from django.db.models.deletion import CASCADE
import numpy
import numpy_hist_io
import csv
import os


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))


class BackgroundProfiles(models.Model):
    BackgroundId = models.IntegerField(primary_key=True)
    BackgroundName = models.CharField(max_length=100)


class BackgroundPowers(models.Model):
    BackgroundPowerId = models.IntegerField(primary_key=True)
    BackgroundId = models.ForeignKey(
        BackgroundProfiles, default=None, on_delete=CASCADE)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)


class ChargingPowers(models.Model):
    Id = models.IntegerField(primary_key=True)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)
