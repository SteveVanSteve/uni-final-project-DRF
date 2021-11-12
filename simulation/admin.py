from django.contrib import admin
from . import models

admin.site.register(models.ArrivalProbabilities)
admin.site.register(models.BackgroundSet)
admin.site.register(models.BackgroundPower)
admin.site.register(models.ChargingCurve)
admin.site.register(models.SimulationConfig)
admin.site.register(models.SimulationResult)

# The SimulationConfig 'POST' the simulated graph (histogram) of the
# combined models that have the data - it will have 'houseId', 'numberOfCars', 'backgroundSetId'
# each field will have respective data

# The post should reply with a SimulationResult object - this will have the fields
# 'time' and 'power'
