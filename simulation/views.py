from django.shortcuts import render
from rest_framework.response import Response
from simulation.models import ArrivalProbabilities
from simulation.serializers import ArrivalProbabilitiesSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from simulation.serializers import UserSerializer
from rest_framework import permissions


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
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]


# still having issues regarding permissions and owners
