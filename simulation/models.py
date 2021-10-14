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


class BackgroundProfiles(models.Model):
    BackgroundId = models.IntegerField(primary_key=True)
    BackgroundName = models.CharField(max_length=200)


class BackgroundPower(models.Model):
    BackgroundPowerId = models.IntegerField(primary_key=True)
    BackgroundId = models.ForeignKey
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)
