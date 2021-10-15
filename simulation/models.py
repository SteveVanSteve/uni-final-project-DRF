from django.db import models
import numpy
import numpy_hist_io
import csv
import os


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))


class BackgroundPowers(models.Model):
    BackgroundPowerId = models.IntegerField(primary_key=True)
    BackgroundId = models.IntegerField(foreignKey=True)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)


class ChargingPowers(models.Model):
    Id = models.IntegerField(primary_key=True)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)
