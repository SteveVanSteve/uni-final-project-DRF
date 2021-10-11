from django.db import models
import numpy
import numpy_hist_io
import csv


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEdge = models.FloatField(null=False)
    binEntry = models.FloatField(null=True)
    hist = (numpy.array([]), numpy.array([]))
