from rest_framework import serializers
from simulation.models import ArrivalProbabilities, ChargingCurve, BackgroundSet, BackgroundPower, SimulationConfig, SimulationResult


class ArrivalProbabilitiesSerializer(serializers.ModelSerializer):
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


class BackgroundSetSerializer(serializers.ModelSerializer):

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


class BackgroundPowerSerializer(serializers.ModelSerializer):

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


class ChargingCurveSerializer(serializers.ModelSerializer):
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


class SimulationConfigSerializer(serializers.ModelSerializer):
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


class SimulationResultSerializer(serializers.ModelSerializer):
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


# Simulation Logic (in the backend)

# (1) Receives the POST simulation run.
# (2) Read all simulation config into memory.
# (3) Read from arrival prob.
# (4) Read from charging curve.
# (5) Read from backgroundSets and backgroundPower.
# (6) Create empty simulation result - all 24hrs, but with zero electric current.
#   - For each house.  (Store these simulation results in a list, where each one corresponds to a houseId)
# (7) Add background into empty data container, using the backgroundSetId to pick the correct one.
#   - For each house.
# (8) Create empty simulation result for all houses.
# (9) For each house:
#       For each car:
#          (a) Find time of arrival.
#          (b) Add the current from the car to the current in the container for this house.
#       Add this house to the total for all houses.
# (10) Save the simulation results to the database.

# The backend needs to be saved so the front end can show the result correctly!
