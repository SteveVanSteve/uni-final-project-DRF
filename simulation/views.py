from django.http.response import Http404
from django.shortcuts import render
from django.views import generic
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from simulation.models import ArrivalProbabilities
from simulation.serializers import ArrivalProbabilitiesSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class ArrivalProbabilitiesList(generics.ListCreateAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer


class ArrivalProbabilitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from simulation.models import *
# from simulation.serializers import ArrivalProbabilitiesSerializer


# @api_view(['GET', 'POST'])
# def ArrivalProbabilities_list(request, format=None):
#     """
#     List all Arrival Probabilities, or create a new Arrival Probability.
#     """
#     if request.method == 'GET':
#         Arrival_Probabilities = ArrivalProbabilities.objects.all()
#         serializer = ArrivalProbabilitiesSerializer(
#             Arrival_Probabilities, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArrivalProbabilitiesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def ArrivalProbabilities_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete an Arrival Probability.
#     """
#     try:
#         Arrival_Probabilities = ArrivalProbabilities.objects.get(pk=pk)
#     except ArrivalProbabilities.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArrivalProbabilitiesSerializer(Arrival_Probabilities)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArrivalProbabilitiesSerializer(
#             Arrival_Probabilities, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         ArrivalProbabilities.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
