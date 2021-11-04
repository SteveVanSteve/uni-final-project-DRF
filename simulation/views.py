from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from simulation.models import ArrivalProbabilities
from simulation.serializers import ArrivalProbabilitiesSerializer


@csrf_exempt
def ArrivalProbabilities_list(request):
    """
    List all Arrival Probabilities, or create a new Arrival Probability.
    """
    if request.method == 'GET':
        Arrival_Probabilities = ArrivalProbabilities.objects.all()
        serializer = ArrivalProbabilitiesSerializer(
            Arrival_Probabilities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArrivalProbabilitiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ArrivalProbabilities_detail(request, pk):
    """
    Retrieve, update or delete an Arrival Probability.
    """
    try:
        Arrival_Probabilities = ArrivalProbabilities.objects.get(pk=pk)
    except ArrivalProbabilities.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArrivalProbabilitiesSerializer(Arrival_Probabilities)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArrivalProbabilitiesSerializer(
            Arrival_Probabilities, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ArrivalProbabilities.delete()
        return HttpResponse(status=204)


# class ArrivalProbabilitiesViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows the Arrival Probabilities to be viewed or edited.
#     """
#     queryset = ArrivalProbabilities.objects.all().order_by('arrivalProbId')
#     serializer_class = ArrivalProbabilitiesSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class ArrivalProbabilitiesList(generics.ListCreateAPIView):
#     queryset = ArrivalProbabilities.objects.all()
#     serializer_class = ArrivalProbabilitiesSerializer
#     pass


# class ArrivalProbabilitiesDetail(generics.RetrieveDestroyAPIView):
#     queryset = ArrivalProbabilities.objects.all()
#     serializer_class = ArrivalProbabilitiesSerializer
#     pass

# class ChargingCurveViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows the Charging Curve to be viewed or edited.
#     """
#     queryset = ChargingCurve.objects.all()
#     serializer_class = ChargingCurveSerializer
#     permission_classes = [permissions.IsAuthenticated]
