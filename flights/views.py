from django.shortcuts import render
from .models import Flight,passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request , "flights/index.html" , 
            {
                "flights" : Flight.objects.all()
            })


def flight(request , flight_id) :
    flight_ = Flight.objects.get(pk = flight_id)
    return render(request , "flights/flight.html" , 
                {
                    "flight" : flight_,
                    "passengers" : flight_.passengers.all(),
                    "non_passengers" : passenger.objects.exclude(flights = flight_id).all()
                    })
def book(request , flight_id):
    if request.method == "POST":
        passenger_id = request.POST["passenger"]
        flight = Flight.objects.filter(pk = flight_id).first()
        Passenger = passenger.objects.filter(pk = passenger_id).first()
        Passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight" , args = (flight.id , )))