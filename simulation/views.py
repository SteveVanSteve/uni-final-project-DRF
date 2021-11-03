from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from simulation.models import ArrivalProbabilities, ChargingCurve
from .serializers import ArrivalProbabilitiesSerializer, ChargingCurveSerializer


class ArrivalProbabilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the Arrival Probabilities to be viewed or edited.
    """
    queryset = ArrivalProbabilities.objects.all().order_by('arrivalProbId')
    serializer_class = ArrivalProbabilitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChargingCurveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the Charging Curve to be viewed or edited.
    """
    queryset = ChargingCurve.objects.all()
    serializer_class = ChargingCurveSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArrivalProbabilitiesList(generics.ListCreateAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    pass


class ArrivalProbabilitiesDetail(generics.RetrieveDestroyAPIView):
    queryset = ArrivalProbabilities.objects.all()
    serializer_class = ArrivalProbabilitiesSerializer
    pass
