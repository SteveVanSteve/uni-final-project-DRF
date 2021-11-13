from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import IntegerField
import numpy

from django.db import models
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))

    def __str__(self):
        return "{}-{}".format(self.arrivalProbId, self.binEntry, self.binEdge)


class BackgroundSet(models.Model):
    backgroundSetId = models.IntegerField(primary_key=True)
    backgroundSetName = models.CharField(max_length=50)

    def __str__(self):
        return "{}-{}".format(self.backgroundSetId, self.backgroundSetName)


class BackgroundPower(models.Model):
    backgroundPowerId = models.IntegerField(primary_key=True)
    backgroundSetId = models.ForeignKey(BackgroundSet, on_delete=PROTECT)
    time = models.FloatField(null=False, default=None)
    power = models.FloatField(null=False, default=None)

    def __str__(self):
        return "{}-{}".format(self.backgroundPowerId, self.backgroundSetId, self.time, self.power)


class ChargingCurve(models.Model):
    chargingCurveId = models.IntegerField(primary_key=True)
    time = models.FloatField(null=False, default=None)
    power = models.FloatField(null=False, default=None)

    def __str__(self):
        return "{}-{}".format(self.chargingCurveId, self.time, self.power)


class SimulationConfig(models.Model):
    houseId = models.IntegerField(null=False)
    numberOfCars = models.IntegerField(null=False)
    backgroundSetId = models.ForeignKey(BackgroundSet, on_delete=PROTECT)

    def __str__(self):
        return "{}-{}".format(self.houseId, self.numberOfCars, self.backgroundSetId)


class SimulationResult(models.Model):
    time = models.FloatField(null=False, default=None)
    power = models.FloatField(null=False, default=None)

    def __str__(self):
        return "{}-{}".format(self.time, self.power)
