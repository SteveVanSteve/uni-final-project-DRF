from simulation.models import ArrivalProbabilities
import numpy
from django.test import TestCase
from django.contrib.auth.models import User
from simulation.models import *


class TestArrivalProbabilities(TestCase):
    def setUp(self):
        print("Setting up test data")
        ArrivalProbabilities.objects.create(
            arrivalProbId=1, binEntry=10, binEdge=4.5)
        ArrivalProbabilities.objects.create(
            arrivalProbId=2, binEntry=27, binEdge=5.5)
        ArrivalProbabilities.objects.create(
            arrivalProbId=3, binEntry=36, binEdge=6.5)
        ArrivalProbabilities.objects.create(
            arrivalProbId=4, binEntry=22, binEdge=7.5)
        ArrivalProbabilities.objects.create(
            arrivalProbId=5, binEntry=5, binEdge=8.5)
        ArrivalProbabilities.objects.create(
            arrivalProbId=6, binEntry=0, binEdge=9.5)

    def test_get_queryset(self):
        query_set = ArrivalProbabilities.objects.all()
        print(query_set)
        n = len(query_set)
        print(n)  # Print each row
        bin_entries = []
        bin_edges = []
        for i in range(n):
            print(query_set[i])
            if query_set[i].binEntry is not None:
                bin_entries.append(query_set[i].binEntry)
            bin_edges.append(query_set[i].binEdge)
        print(bin_entries, bin_edges)

        hist = (numpy.array(bin_entries), numpy.array(bin_edges))

    def test_get_queryset_sanity_check(self):
        print("Hello Steve!")
        i = 1
        self.assertEqual(i, 1)
        l = [3, 4]
        self.assertIn(4, l)


class TestChargingCurve(TestCase):
    def test_charging_curve(self):
        print("")
        i = 2
        self.assertEqual(i, 2)
        l = [5, 6]
        self.assertIn(6, l)
