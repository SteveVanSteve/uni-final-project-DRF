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


# The Simulation Result has to be an APIView
class SimulationResultViewSet(APIView):

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
        # For each house we need to get the background data

        # -Create a total (empty) power verses time structure in memory for all houses.
        # Delete Previous Simulation
        SimulationResult.objects.all().delete()
        # Create  new result with 0 as initial power
        currentTime = 0.00
        for i in range(24):
            SimulationResult.objects.create(time=currentTime, power=0.0)
            currentTime += 1.00

        # Loop over all of the houses:
            # This is an example of looping over each house in the config and printing the data
        for house in serializedSimulationConfigs:
            print("\n House:")
            print("HouseId: " + str(house['houseId']))
            print("numberOfCars: " + str(house['numberOfCars']))
            print("backgroundSet: " + str(house['backgroundSetId']))

            # -Create a power verses time structure in memory for this house.
            # Unsure what this should look like,
            # We want to create an empty list for the house(?)
            powerTimeStruct = []
            currentTime = 0.00
            for i in range(24):
                powerTime = {"time": currentTime, "power": 0.0}
                powerTimeStruct.append(powerTime)
                currentTime += 1.00
            print('powerTimeStruct:')
            print(powerTimeStruct)

            # -Add the power verses time from the background table to the house.

            # For each hour in the houses power time structure
            # length = len(powerTimeStruct)
            # powerTimexWithBackground=powerTimeStruct
            # for powerTimex in powerTimeStruct:
            #     #Get the current time in loop and filter background power for this set and time
            #     print(powerTimex)

            #     timex=powerTimex.get('time')
            #     initialPower=powerTimex.get('power')

            #     backgroundPower = BackgroundPower.objects.filter(backgroundSetId=house['backgroundSetId'], time=timex)
            #     print('backgroundsets with id:'+str(house['backgroundSetId']) + 'and time: '+str(timex))
            #     if backgroundPower:
            #         newPowerTime={"time": timex, "power": initialPower+backgroundPower.first().power}
            #         print(newPowerTime)
            #         #powerTimexWithBackground.insert(i,newPowerTime )
            # print('powerTimeStruct with background set added:')
            # print(powerTimeStruct)

            # -Loop over each car:
            for i in range(house['numberOfCars']):
                print("Looping over another car: " + str(i))
                #  i.      Use the arrival probability curve to find when the driver returns home.
                # ii.      Add the power verses time curve to the house.

            # -Add the power verses time curve for this house to the total for all houses.
            # Need to add the each power and time value to the total already in Simlation Result

        # Return the total power verses time curve back to the user interface.
        simulationResults = SimulationResult.objects.all()
        serializer = SimulationResultSerializer(simulationResults, many=True)
        return Response(status=status.HTTP_200_OK, data={"success": "SimulationResult created successfully", "data": serializer.data})
