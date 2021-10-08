from django.db import models


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEdge = models.FloatField(null=False)
    binEntry = models.FloatField(null=True)
