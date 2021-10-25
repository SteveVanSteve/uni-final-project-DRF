from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models import ChargingCurve
import numpy
import numpy_hist_io
import csv
import os


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEntry = models.FloatField(null=True)
    binEdge = models.FloatField(null=False)
    hist = (numpy.array(binEntry), numpy.array(binEdge))


class ChargingCurve(models.Model):
    # Read all of the data.
    query_set = ChargingCurve.object.all()
# Print each column for each row.
    for row in query_set:
        print(row.time)
        print(row.power)
