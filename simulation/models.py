from django.db import models
from django.utils.translation import gettext as _
import numpy
import numpy_hist_io
import csv


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(
        primary_key=True), default = None, (_("Arrival Probability ID"))
    binEdge = models.FloatField(null=False), (_("Bin Edge"))
    binEntry = models.FloatField(null=True), (_("Bin Entry"))
    hist = (numpy.array([]), numpy.array([]))
