from django.db.models.expressions import F
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
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
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.reverse import reverse
import random


class ArrivalProbabilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ArrivalProbabilities to be viewed or edited.
    """
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    permission_classes = []
    authentication_classes = []


class BackgroundSetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackgroundSet to be viewed or edited.
    """
    queryset = BackgroundSet.objects.all()
    serializer_class = BackgroundSetSerializer
    permission_classes = []
    authentication_classes = []


class BackgroundPowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackgroundPowers to be viewed or edited.
    """
    queryset = BackgroundPower.objects.all()
    serializer_class = BackgroundPowerSerializer
    permission_classes = []
    authentication_classes = []


class ChargingCurveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ChargingCurves to be viewed or edited.
    """
    queryset = ChargingCurve.objects.all()
    serializer_class = ChargingCurveSerializer
    permission_classes = []
    authentication_classes = []


class SimulationConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SimulationConfig to be viewed or edited.
    """
    queryset = SimulationConfig.objects.all()
    serializer_class = SimulationConfigSerializer
    permission_classes = []
    authentication_classes = []


class SimulationResultViewSet(APIView):
    """
    API endpoint that allows SimulationResult to be viewed.
    """

    def get(self, request):
        simulationResults = SimulationResult.objects.all()
        serializer = SimulationResultSerializer(simulationResults, many=True)
        return Response({"SimulationResult": serializer.data})

    def post(self, request):
        simulationConfigs = request.data
        configSerializer = SimulationConfigSerializer(
            data=simulationConfigs, many=True)
        if not configSerializer.is_valid():
            print("Data is not valid")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"failure:" "Data is not valid"})
        serializedSimulationConfigs = configSerializer.data

        SimulationResultUtils.resetSimulationResult()

        for house in serializedSimulationConfigs:
            SimulationResultUtils.printHouse(house)
            powerTimeStruct = SimulationResultUtils.createEmptyPowerStruct()
            powerTimeStruct = SimulationResultUtils.addPowerFromBackgroundSet(
                house['backgroundSetId'], powerTimeStruct)

            for i in range(house['numberOfCars']):
                print("Looping over another car: " + str(i))

                carArrivalTime = SimulationResultUtils.getArrivalTimeFromProbability()
                print("Car arrival time predicted as " + str(carArrivalTime))

                powerTimeStruct = SimulationResultUtils.addPowerFromCharginCurve(
                    carArrivalTime, powerTimeStruct)

            SimulationResultUtils.addHousePowerToSimulationResult(
                powerTimeStruct)

        simulationResults = SimulationResult.objects.all()
        serializer = SimulationResultSerializer(simulationResults, many=True)
        return Response(status=status.HTTP_200_OK, data={"success": "SimulationResult created successfully", "data": serializer.data})


class SimulationResultUtils():

    def resetSimulationResult():

        SimulationResult.objects.all().delete()

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

    def addPowerFromCharginCurve(startTimeOffset, powerTimeStruct):
        updatedPowerTimeStruct = powerTimeStruct.copy()

        count = 0
        for hour in powerTimeStruct:

            initialPower = hour.get('power')
            hourTime = hour.get('time')
            minTime = hourTime-startTimeOffset
            maxTime = minTime + 1

            chargingCurveFilteredByHour = ChargingCurve.objects.filter(
                time__gte=minTime, time__lte=maxTime)
            if chargingCurveFilteredByHour:
                totalPowerToAdd = 0

                for powerToAdd in chargingCurveFilteredByHour:
                    totalPowerToAdd += powerToAdd.power

                newPowerTime = {"time": hourTime,
                                "power": initialPower+totalPowerToAdd}
                updatedPowerTimeStruct[count] = newPowerTime
            count += 1
        print('powerTimeStruct with charging curve added:')
        print(updatedPowerTimeStruct)
        return updatedPowerTimeStruct

    def addHousePowerToSimulationResult(powerTimeStruct):

        for hour in powerTimeStruct:
            SimulationResult.objects.filter(time=hour.get('time')).update(
                power=F('power') + hour.get('power'))

    def getArrivalTimeFromProbability():
        randomInt = random.randint(1, 100)
        arrivalProbabilities = ArrivalProbabilities.objects.all()
        lastEntry = 0
        for arrivalProbability in arrivalProbabilities:
            entry = arrivalProbability.binEntry + lastEntry
            if lastEntry <= randomInt <= entry:
                print("Arrival time chosen is: " +
                      str(arrivalProbability.binEdge))

                return arrivalProbability.binEdge
            else:
                lastEntry = entry
