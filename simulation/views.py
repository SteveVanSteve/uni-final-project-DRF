from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from simulation.models import ArrivalProbabilities, ChargingCurve
from simulation.permissions import IsOwnerOrReadOnly
from simulation.serializers import ArrivalProbabilitiesSerializer, ChargingCurveSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from simulation.serializers import UserSerializer
from rest_framework import permissions
from simulation.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'simulation': reverse('arrivalprobabilities-list', request=request, format=format),
        'simulation': reverse('chargingcurve-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArrivalProbabilitiesList(generics.ListCreateAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArrivalProbabilitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChargingCurveList(generics.ListCreateAPIView):
    queryset = ChargingCurve.objects.all()
    serializer_class = ChargingCurveSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChargingCurveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargingCurve.objects.all()
    serializer_class = ChargingCurveSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
