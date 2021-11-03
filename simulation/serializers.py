from rest_framework import serializers
from simulation.models import ArrivalProbabilities, ChargingCurve


class ArrivalProbabilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArrivalProbabilities
        fields = ['arrivalProbId', 'binEntry', 'binEdge']


class ChargingCurveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChargingCurve
        fields = ['chargingCurveId', 'times', 'powers']
