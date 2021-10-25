# Test Arrival Probabilities
# By Steve Shields

from django.test import TestCase

from simulation.models import ArrivalProbabilities


class ArrivalProbabilitiesTestCase(TestCase):
    def setUp(self):
        ArrivalProbabilities.objects.create()
