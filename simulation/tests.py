# Test Arrival Probabilities
# By Steve Shields

import numpy
from django.test import TestCase
from simulation.models import ArrivalProbabilities


class TestArrivalProbabilities(TestCase):
    def test_get_queryset_test(self):
        print("Hello Steve!")
        i = 1
        self.assertEqual(i, 1)
        l = [3, 4]
        self.assertIn(4, l)

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
