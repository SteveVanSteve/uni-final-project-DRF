from rest_framework import serializers
from simulation.models import ArrivalProbabilities
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    simulation = serializers.HyperlinkedRelatedField(
        many=True, view_name='arrivalprobabilities-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'simulation', 'owner']


class ArrivalProbabilitiesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ArrivalProbabilities
        fields = ['url', 'owner', 'arrivalProbId', 'binEntry', 'binEdge']

    def create(self, validated_data):
        return ArrivalProbabilities.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.arrivalProbId = validated_data.get(
            'arrivalProbId', instance.arrivalProbId)
        instance.binEntry = validated_data.get('binEntry', instance.binEntry)
        instance.binEdge = validated_data.get('binEdge', instance.binEdge)
        instance.save()
        return instance
