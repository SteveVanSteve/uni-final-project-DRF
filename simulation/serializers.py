from rest_framework import serializers
from simulation.models import ArrivalProbabilities, ChargingCurve, BackgroundSet, BackgroundPower, SimulationConfig, SimulationResult

# insert SimulationConfig and SimulationResult classes as serializer models
# and get them to hook up to the API


class ArrivalProbabilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArrivalProbabilities
        fields = ['arrivalProbId', 'binEntry', 'binEdge']

    def create(self, validated_data):
        return ArrivalProbabilities.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.arrivalProbId = validated_data.get(
            'arrivalProbId', instance.arrivalProbId)
        instance.binEntry = validated_data.get('binEntry', instance.binEntry)
        instance.binEdge = validated_data.get('binEdge', instance.binEdge)
        instance.save()
        return instance


class BackgroundSetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BackgroundSet
        fields = ['backgroundSetId', 'backgroundSetName']

    def create(self, validated_data):
        return BackgroundSet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.backgroundSetId = validated_data.get(
            'backgroundSetId', instance.backgroundSetId)
        instance.backgroundSetName = validated_data.get(
            'backgroundSetName', instance.backgroundSetName)
        instance.save()
        return instance


class BackgroundPowerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BackgroundPower
        fields = ['backgroundPowerId', 'backgroundSetId', 'time', 'power']

    def create(self, validated_data):
        return BackgroundPower.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.backgroundPowerId = validated_data.get(
            'backgroundPowerId', instance.backgroundPowerId)
        instance.backgroundSetId = validated_data.get(
            'backgroundSetId', instance.backgroundSetId)
        instance.time = validated_data.get('time', instance.time)
        instance.power = validated_data.get('power', instance.power)
        instance.save()
        return instance


class ChargingCurveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChargingCurve
        fields = ['chargingCurveId', 'time', 'power']

    def create(self, validated_data):
        return ChargingCurve.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.chargingCurveId = validated_data.get(
            'chargingCurveId', instance.chargingCurveId)
        instance.time = validated_data.get('time', instance.time)
        instance.power = validated_data.get('power', instance.power)
        instance.save()
        return instance


class SimulationConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimulationConfig
        fields = ['houseId', 'numberOfCars', 'backgroundSetId']

    def create(self, validated_data):
        return SimulationConfig.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.houseId = validated_data.get('houseId', instance.houseId)
        instance.numberOfCars = validated_data.get(
            'numberOfCars', instance.numberOfCars)
        instance.backgroundSetId = validated_data.get(
            'backgroundSetId', instance.backgroundSetId)
        instance.save()
        return instance


class SimulationResultSerializer(serializers.Serializer):
    class Meta:
        model = SimulationResult
        fields = ['time', 'power']

    def create(self, validated_data):
        return SimulationResult.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.time = validated_data.get('time', instance.time)
        instance.power = validated_data.get('power', instance.power)
        instance.save()
        return instance
