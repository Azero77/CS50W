
#it is similar class to what we have know about unittest
from django.test import TestCase , Client
from .models import *
from django.db.models import Max

# Create your tests here.

class FlightTestCase(TestCase):
    def setUP(self):
        #add samples to the dataset(not the userdata)
        #it is a data specific to test and it is deleted automatically after using test
        a1 = airport.objects.create(code = "AAA" , city = "City A")
        a2 = airport.objects.create(code = "BBB" , city = "City B")
        #creating FLight
        Flight.objects.create(origin = a1 , destination = a2 , duration = 200)
        Flight.objects.create(origin = a1 , destination = a1 , duration = 200)
        Flight.objects.create(origin = a1 , destination = a2 , duration = -4)
    def deparuters_count(self):
        a1 = airport.objects.get(code = "AAA" , city = "City A")
        dep_a = a1.departures.count()
        self.assertEqual(dep_a , 3)
    def arrivals_count(self):
        a1 = airport.objects.get(code = "AAA")
        self.assertEqual(a1.arrivals.count() , 1)
    def test_valid_flight(self):
        # a1 = airport.objects.get(code = "AAA" , city = "City A")
        a2 = airport.objects.get(code = "BBB")
        f = Flight.objects.get(origin = a2 , destination = a2 , duration = 200)
        self.assertTrue(f.flight_is_valid())
    def test_invalid_flight_destination(self):
        a1 = airport.objects.get(code = "AAA")
        f = Flight.objects.get(origin = a1 , destination = a1 , duration = 200)
        self.assertFalse(f.flight_is_valid())
    def test_invalid_flight_destination(self):
        a1 = airport.objects.get(code = "AAA")
        a2 = airport.objects.get(code = "BBB")
        f = Flight.objects.get(origin = a1 , destination = a2 , duration = -4)
        self.assertFalse(f.flight_is_valid())
    