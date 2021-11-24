from django.db.models.expressions import F
from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import views
from rest_framework.response import Response
from django.views.generic import TemplateView
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


class SimulationResultViewSet(APIView):
    """
    API endpoint that allows SimulationResult to be viewed.
    """

    def get(self, request):
        # Return the last simulation result
        simulationResults = SimulationResult.objects.all()
        serializer = SimulationResultSerializer(simulationResults, many=True)
        return Response({"SimulationResult": serializer.data})

    def post(self, request):
        simulationConfigs = request.data
        # Deserialize the JSON.
        configSerializer = SimulationConfigSerializer(
            data=simulationConfigs, many=True)
        if not configSerializer.is_valid():
            print("Data is not valid")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"failure:" "Data is not valid"})
        serializedSimulationConfigs = configSerializer.data

        # -Get the data from the MariaDB database.
        # andrew: What data?, I am guessing for each house we neec to get the background data? WHat else?

        # -Create a total (empty) power verses time structure in memory for all houses.
        # andrew: Maybe this just means deleted the current Simulation Result model data?
        SimulationResultUtils.resetSimulationResult()

        # Loop over all of the houses:
        for house in serializedSimulationConfigs:
            SimulationResultUtils.printHouse(house)
            # -Create a power verses time structure in memory for this house.
            powerTimeStruct = SimulationResultUtils.createEmptyPowerStruct()

            # -Add the power verses time from the background table to the house.
            powerTimeStruct = SimulationResultUtils.addPowerFromBackgroundSet(
                house['backgroundSetId'], powerTimeStruct)

            # -Loop over each car:
            # todo: implement arrival probability
            for i in range(house['numberOfCars']):
                print("Looping over another car: " + str(i))
                #  i.      Use the arrival probability curve to find when the driver returns home.
                # ii.      Add the power verses time curve to the house.

            # -Add the power verses time curve for this house to the total for all houses.
            SimulationResultUtils.addHousePowerToSimulationResult(
                powerTimeStruct)

        # Return the total power verses time curve back to the user interface.
        simulationResults = SimulationResult.objects.all()
        serializer = SimulationResultSerializer(simulationResults, many=True)
        return Response(status=status.HTTP_200_OK, data={"success": "SimulationResult created successfully", "data": serializer.data})


class SimulationResultUtils():

    # Have abstracted the methods used to make the code tidier / clearer and also makes the code more testable.
    # Each of these methods could be unit tested

    def resetSimulationResult():
        # Delete Previous Simulation
        SimulationResult.objects.all().delete()
        # Create  new result with 0 as initial power
        currentTime = 0.00
        for i in range(24):
            SimulationResult.objects.create(time=currentTime, power=0.0)
            currentTime += 1.00

    def printHouse(house):
        print("\n House:")
        print("HouseId: " + str(house['houseId']))
        print("numberOfCars: " + str(house['numberOfCars']))
        print("backgroundSet: " + str(house['backgroundSetId']))

    def createEmptyPowerStruct():
        powerTimeStruct = []
        currentTime = 0.00
        # For every hour in 1 day create a new empty item in powerTimeStruct
        for i in range(24):
            powerTime = {"time": currentTime, "power": 0.0}
            powerTimeStruct.append(powerTime)
            currentTime += 1.00
        print('powerTimeStruct:')
        print(powerTimeStruct)
        return powerTimeStruct

    def addPowerFromBackgroundSet(backgroundSetId, powerTimeStruct):
        count = 0
        updatedPowerTimeStruct = powerTimeStruct.copy()
        for hour in powerTimeStruct:
            # Get the current time in loop and filter background power for this set and time
            time = hour.get('time')
            initialPower = hour.get('power')
            backgroundPower = BackgroundPower.objects.filter(
                backgroundSetId=backgroundSetId, time=time)
            if backgroundPower:
                newPowerTime = {
                    "time": time, "power": initialPower+backgroundPower.first().power}
                updatedPowerTimeStruct[count] = newPowerTime
            count += 1
        print('powerTimeStruct with background set added:')
        print(updatedPowerTimeStruct)
        return updatedPowerTimeStruct

    def addHousePowerToSimulationResult(powerTimeStruct):
        # For each hour in the powerTimeStruct lets update the total power in SimulationResult
        for hour in powerTimeStruct:
            SimulationResult.objects.filter(time=hour.get('time')).update(
                power=F('power') + hour.get('power'))
