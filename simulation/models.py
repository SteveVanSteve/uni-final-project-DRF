from django.db import models
from django.db.models.fields import IntegerField
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))
    owner = models.ForeignKey(
        'auth.user', related_name='simulation', on_delete=models.CASCADE)

    class Meta:
        ordering = ['arrivalProbId']


# class BackgroundSets(models.Model):
#     Id = models.IntegerField(primary_key=True)
#     Name = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         ordering = ['Name']


# class Backgrounds(models.Model):
#     Id = models.IntegerField(primary_key=True)
#     BackgroundSetId = models.ForeignKey(
#         BackgroundSets, default=1, on_delete=models.SET_DEFAULT)
#     Time = models.FloatField(null=False)
#     Power = models.FloatField(null=False)

#     class Meta:
#         ordering = ['Id']


# class ChargingCurve(models.Model):
#     chargingCurveId = models.IntegerField(primary_key=True)
#     Time = models.FloatField(null=False)
#     Power = models.FloatField(null=False)

#     class Meta:
#         ordering = ['chargingCurveId']
