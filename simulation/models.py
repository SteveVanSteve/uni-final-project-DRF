from django.db import models
from django.db.models.fields import IntegerField
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))
    owner = models.ForeignKey(
        'auth.user', related_name='simulation', on_delete=models.PROTECT)

    class Meta:
        ordering = ['arrivalProbId']


class ChargingCurve(models.Model):
    chargingCurveId = models.IntegerField(primary_key=True)
    Time = models.FloatField(null=False)
    Power = models.FloatField(null=False)

    class Meta:
        ordering = ['chargingCurveId']
