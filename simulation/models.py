from django.db import models
import csv
import os
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEdge = models.FloatField(null=False)
    binEntry = models.FloatField(null=True)
    hist = (numpy.array([]), numpy.array([]))
