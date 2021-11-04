from simulation.models import ArrivalProbabilities, ChargingCurve, BackgroundSets, Backgrounds
import numpy
import time
from django.test import TestCase
from django.contrib.auth.models import User
from simulation.models import *


class TestArrivalProbabilities(TestCase):
    def test_get_queryset_sanity_check(self):
        print("Hello Steve!")
        i = 1
        self.assertEqual(i, 1)
        l = [3, 4]
        self.assertIn(4, l)

    def setUp(self):
        print("Set up Arrival Probability test data")
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
        self.assertEqual(n, 6)
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
        print(hist)


class TestChargingCurve(TestCase):
    def setUp(self):
        print("Get and check the Charging Curve data")
        ChargingCurve.objects.create(
            chargingCurveId=1, Time=00.00, Power=81.3008)
        ChargingCurve.objects.create(
            chargingCurveId=2, Time=00.10, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=3, Time=00.30, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=4, Time=00.35, Power=8658.54)
        ChargingCurve.objects.create(
            chargingCurveId=5, Time=00.40, Power=10772.4)
        ChargingCurve.objects.create(
            chargingCurveId=6, Time=00.45, Power=11016.3)
        ChargingCurve.objects.create(
            chargingCurveId=7, Time=1.00, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=8, Time=1.05, Power=6707.32)
        ChargingCurve.objects.create(
            chargingCurveId=9, Time=1.10, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=10, Time=1.30, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=11, Time=1.35, Power=9308.94)
        ChargingCurve.objects.create(
            chargingCurveId=12, Time=1.45, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=13, Time=2.00, Power=10853.7)
        ChargingCurve.objects.create(
            chargingCurveId=14, Time=2.05, Power=8333.33)
        ChargingCurve.objects.create(
            chargingCurveId=15, Time=2.10, Power=10935)
        ChargingCurve.objects.create(
            chargingCurveId=16, Time=2.30, Power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=17, Time=2.35, Power=5934.96)
        ChargingCurve.objects.create(
            chargingCurveId=18, Time=2.40, Power=4471.54)
        ChargingCurve.objects.create(
            chargingCurveId=19, Time=2.45, Power=3739.84)
        ChargingCurve.objects.create(
            chargingCurveId=20, Time=2.50, Power=1910.57)
        ChargingCurve.objects.create(
            chargingCurveId=21, Time=2.55, Power=1300.81)
        ChargingCurve.objects.create(
            chargingCurveId=22, Time=3.01, Power=162.602)

    def test_get_queryset_charging_curve(self):
        query_set = ChargingCurve.objects.all()
        print(query_set)
        n = len(query_set)
        self.assertEqual(n, 22)
        print(n)
        times = []
        powers = []
        for i in range(n):
            print(query_set[i])
            times.append(query_set[i].Time)
            powers.append(query_set[i].Power)
        print(times, powers)


class TestBackgroundSets(TestCase):
    def setUp(self):
        print("Getting and checking the Background Sets data")
        BackgroundSets.objects.create(Id=1, Name="No Electric Heating")
        BackgroundSets.objects.create(Id=2, Name="Additional Electric Heating")
        BackgroundSets.objects.create(Id=3, Name="Primary Electric Heating")

    def test_get_queryset_background_sets(self):
        query_set = BackgroundSets.objects.all()
        print(query_set)
        n = len(query_set)
        self.assertEqual(n, 3)
        print(n)
        background_set_id = []
        background_set_name = []
        for i in range(n):
            print(query_set[i])
            background_set_id.append(query_set[i].Id)
            background_set_name.append(query_set[i].Name)
        print(background_set_id, background_set_name)


class TestBackgrounds(TestCase):
    def setUp(self):
        print("Getting and checking the backgrounds data")
        Backgrounds.objects.create(
            Id=4, BackgroundSetId=1, Time=00.00, Power=256.667)

    def test_get_queryset_backgrounds(self):
        query_set = Backgrounds.objects.all()
        print(query_set)
        n = len(query_set)
        self.assertEqual(n, 1)
        print(n)
        backgrounds_id = []
        background_set_id = []
        times = []
        powers = []
        for i in range(n):
            print(query_set[i])
            backgrounds_id.append(query_set[i].Id)
            background_set_id.append(query_set[i].BackgroundSetId)
            times.append(query_set[i].Time)
            powers.append(query_set[i].Power)
            print(backgrounds_id, background_set_id, times, powers)
