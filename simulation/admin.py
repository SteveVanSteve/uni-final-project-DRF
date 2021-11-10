from django.contrib import admin
from numpy import mod
from . import models

admin.site.register(models.ArrivalProbabilities)
admin.site.register(models.BackgroundSet)
admin.site.register(models.BackgroundPower)
admin.site.register(models.ChargingCurve)
