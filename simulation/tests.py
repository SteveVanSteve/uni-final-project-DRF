# Test Arrival Probabilities
# By Steve Shields
import numpy
from django.db.models import query
from django.test import TestCase
from simulation.models import ArrivalProbabilities


class TestArrivalProbabilities(TestCase):
    def test_get_queryset(self):
        print("Ok! Let's read some data and make a graph!")
        i = 1
        self.assertEqual(i, 1)
        l = [3, 4]
        self.assertIn(4, l)

    def test_get_queyset(self):
        query_set = ArrivalProbabilities.objects.all()
        print(query_set)
        n = len(query_set)
        print(n)
        bin_entries = []
        bin_edges = []
        for i in range(n):
            print(query_set[i])  # Print each row
            if query_set[i].binEntry is not None:
                bin_entries.append(query_set[i].binEntry)
            bin_edges.append(query_set[i].binEdge)
        print(bin_entries, bin_edges)

        hist = (numpy.array(bin_entries), numpy.array(bin_edges))
