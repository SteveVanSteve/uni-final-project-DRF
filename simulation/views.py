from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import views
from rest_framework.response import Response
import simulation
from .models import ArrivalProbabilities, BackgroundSet, BackgroundPower, ChargingCurve, SimulationConfig, SimulationResult
from simulation.permissions import IsOwnerOrReadOnly
from .serializers import ArrivalProbabilitiesSerializer, BackgroundSetSerializer, BackgroundPowerSerializer, ChargingCurveSerializer, SimulationConfigSerializer, SimulationResultSerializer
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


class SimulationConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SimulationConfig to be viewed or edited.
    """
    queryset = SimulationConfig.objects.all()
    serializer_class = SimulationConfigSerializer
    permission_classes = [permissions.IsAuthenticated]


class SimulationResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SimulationResult to be viewed.
    """
    queryset = SimulationResult.objects.all()
    serializer_class = SimulationResultSerializer
    permission_classes = [permissions.IsAuthenticated]


# @api_view(['GET', 'POST'])
# def simulationConfig_list(request):
#     """
#     List all the details of the existing SimulationConfig, or create a new SimulationConfig.
#     """
#     if request.method == 'GET':
#         simulation = SimulationConfig.objects.all()
#         serializer = SimulationConfigSerializer(simulation, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SimulationConfigSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
