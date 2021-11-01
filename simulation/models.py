from django.db import models
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))


class ChargingCurve(models.Model):
    chargingCurveId = models.IntegerField(primary_key=True)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)
