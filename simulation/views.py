from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from .models import ArrivalProbabilities, BackgroundSet, BackgroundPower, ChargingCurve
from simulation.permissions import IsOwnerOrReadOnly
from .serializers import ArrivalProbabilitiesSerializer, BackgroundSetSerializer, BackgroundPowerSerializer, ChargingCurveSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from simulation.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# query =
# serializer_class =
# context = {'serializer_class_data': serializer_class.data}
# return Response


class ArrivalProbabilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ArrivalProbabilities to be viewed or edited.
    """
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class BackgroundSetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackgroundSet to be viewed or edited.
    """
    queryset = BackgroundSet.objects.all()
    serializer_class = BackgroundSetSerializer
    permission_classes = [permissions.IsAuthenticated]


class BackgroundPowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackgroundPowers to be viewed or edited.
    """
    queryset = BackgroundPower.objects.all()
    serializer_class = BackgroundPowerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChargingCurveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ChargingCurves to be viewed or edited.
    """
    queryset = ChargingCurve.objects.all()
    serializer_class = ChargingCurveSerializer
    permission_classes = [permissions.IsAuthenticated]
