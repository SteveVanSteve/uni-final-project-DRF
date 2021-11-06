from rest_framework import serializers
from simulation.models import ArrivalProbabilities
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    simulation = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ArrivalProbabilities.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'simulation', 'owner']


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
