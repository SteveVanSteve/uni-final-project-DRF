from django.test import TestCase
from simulation.models import ArrivalProbabilities, BackgroundSet, BackgroundPower, ChargingCurve
import numpy


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
            chargingCurveId=1, time=00.00, power=81.3008)
        ChargingCurve.objects.create(
            chargingCurveId=2, time=00.10, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=3, time=00.30, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=4, time=00.35, power=8658.54)
        ChargingCurve.objects.create(
            chargingCurveId=5, time=00.40, power=10772.4)
        ChargingCurve.objects.create(
            chargingCurveId=6, time=00.45, power=11016.3)
        ChargingCurve.objects.create(
            chargingCurveId=7, time=1.00, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=8, time=1.05, power=6707.32)
        ChargingCurve.objects.create(
            chargingCurveId=9, time=1.10, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=10, time=1.30, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=11, time=1.35, power=9308.94)
        ChargingCurve.objects.create(
            chargingCurveId=12, time=1.45, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=13, time=2.00, power=10853.7)
        ChargingCurve.objects.create(
            chargingCurveId=14, time=2.05, power=8333.33)
        ChargingCurve.objects.create(
            chargingCurveId=15, time=2.10, power=10935)
        ChargingCurve.objects.create(
            chargingCurveId=16, time=2.30, power=10975.6)
        ChargingCurve.objects.create(
            chargingCurveId=17, time=2.35, power=5934.96)
        ChargingCurve.objects.create(
            chargingCurveId=18, time=2.40, power=4471.54)
        ChargingCurve.objects.create(
            chargingCurveId=19, time=2.45, power=3739.84)
        ChargingCurve.objects.create(
            chargingCurveId=20, time=2.50, power=1910.57)
        ChargingCurve.objects.create(
            chargingCurveId=21, time=2.55, power=1300.81)
        ChargingCurve.objects.create(
            chargingCurveId=22, time=3.01, power=162.602)

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
            times.append(query_set[i].time)
            powers.append(query_set[i].power)
        print(times, powers)


class TestBackgroundSet(TestCase):
    def setUp(self):
        print("Getting and checking the Background Set data for all three settings")
        BackgroundSet.objects.create(
            backgroundSetId=1, backgroundSetName="No Electric Heating")
        BackgroundSet.objects.create(
            backgroundSetId=2, backgroundSetName="Additional Electric Heating")
        BackgroundSet.objects.create(
            backgroundSetId=3, backgroundSetName="Primary Electric Heating")

    def test_get_queryset_background_sets(self):
        query_set = BackgroundSet.objects.all()
        print(query_set)
        n = len(query_set)
        self.assertEqual(n, 3)
        print(n)
        background_set_id = []
        background_set_name = []
        for i in range(n):
            print(query_set[i])
            background_set_id.append(query_set[i].backgroundSetId)
            background_set_name.append(query_set[i].backgroundSetName)
        print(background_set_id, background_set_name)


# class TestBackgroundPower(TestCase):
#     def setUp(self):
#         print("Getting and checking the background power data")
#         BackgroundSet.objects.create(
#             backgroundSetId=1, backgroundSetName="No Electric Heating")
#         BackgroundPower.objects.create(
#             backgroundPowerId=1, backgroundSetId=1, time=00.00, power=256.667)

#     def test_get_queryset_backgrounds(self):
#         query_set = BackgroundPower.objects.all()
#         print(query_set)
#         n = len(query_set)
#         self.assertEqual(n, 1)
#         print(n)
#         backgrounds_id = []
#         background_set_id = []
#         times = []
#         powers = []
#         for i in range(n):
#             print(query_set[i])
#             backgrounds_id.append(query_set[i].backgroundPowerId)
#             background_set_id.append(query_set[i].backgroundSetId)
#             times.append(query_set[i].time)
#             powers.append(query_set[i].power)
#         print(backgrounds_id, background_set_id, times, powers)
