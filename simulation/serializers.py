from rest_framework import serializers
from simulation.models import *


class ArrivalProbabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArrivalProbabilities
        fields = ['arrivalProbId', 'binEntry', 'binEdge']


class BackgroundSetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BackgroundSets
        fields = ['No Electric Heating',
                  'Additional Electric Heating', 'Primary Electric Heating']


class BackgroundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backgrounds
        fields = ['Id', 'BackgroundSetId', 'Time', 'Power']


class ChargingCurveSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargingCurve
        fields = ['chargingCurveId', 'Times', 'Powers']
