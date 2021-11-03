from rest_framework import serializers
from simulation.models import ArrivalProbabilities, ChargingCurve


class ArrivalProbabilitiesSerializer(serializers.HyperlinkedModelSerializer):
    arrivalProbId = serializers.IntegerField(read_only=True)
    binEntry = serializers.FloatField(read_only=True)
    binEdge = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Arrival Probabilities` instance, given the validated data.
        """
        return ArrivalProbabilities.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new `Arrival Probabilities` instance, given the validated data.
        """
        instance.arrivalProbId = validated_data.get(
            'arrivalProbId', instance.arrivalProbId)
        instance.binEntry = validated_data.get('binEntry', instance.binEntry)
        instance.binEdge = validated_data.get('binEdge', instance.binEdge)
        instance.save()
        return instance

    class Meta:
        model = ArrivalProbabilities
        fields = ['arrivalProbId', 'binEntry', 'binEdge']


class ChargingCurveSerializer(serializers.HyperlinkedModelSerializer):
    chargingCurveId = serializers.IntegerField(read_only=True)
    Time = serializers.FloatField(read_only=True)
    Power = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Charging Curve` instance, given the validated data.
        """
        return ChargingCurve.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new `Arrival Probabilities` instance, given the validated data.
        """
        instance.chargingCurveId = validated_data.get(
            'chargingCurveId', instance.chargingCurveId)
        instance.Time = validated_data.get('times', instance.Time)
        instance.Power = validated_data.get('powers', instance.Power)
        instance.save()
        return instance

    class Meta:
        model = ChargingCurve
        fields = ['chargingCurveId', 'times', 'powers']
