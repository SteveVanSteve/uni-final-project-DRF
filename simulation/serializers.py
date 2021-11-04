from rest_framework import serializers
from simulation.models import ArrivalProbabilities, BackgroundSets, Backgrounds, ChargingCurve


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


class BackgroundSetsSerializer(serializers.HyperlinkedModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `BackgroundSets` instance, given the validated data - i.e the different scenarios.
        """
        return BackgroundSets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new `BackgroundSets` instance, given the validated data.
        """
        instance.Id = validated_data.get(
            'Id', instance.Id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

    class Meta:
        model = BackgroundSets
        fields = ['No Electric Heating',
                  'Additional Electric Heating', 'Primary Electric Heating']


class BackgroundsSerializer(serializers.HyperlinkedModelSerializer):
    Id = serializers.IntegerField(read_only=True)
    BackgroundSetId = serializers.FloatField(read_only=True)
    Time = serializers.FloatField(read_only=True)
    Power = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Backgrounds` instance, given the validated data.
        """
        return Backgrounds.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new `Backgrounds` instance, given the validated data.
        """
        instance.Id = validated_data.get(
            'Id', instance.Id)
        instance.BackgroundSetId = validated_data.get(
            'BackgroundSetId', instance.BackgroundSetId)
        instance.Time = validated_data.get('Time', instance.Time)
        instance.save()
        return instance

    class Meta:
        model = Backgrounds
        fields = ['Id', 'BackgroundSetId', 'Time', 'Power']


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
        instance.Time = validated_data.get('Times', instance.Time)
        instance.Power = validated_data.get('Powers', instance.Power)
        instance.save()
        return instance

    class Meta:
        model = ChargingCurve
        fields = ['chargingCurveId', 'Times', 'Powers']
