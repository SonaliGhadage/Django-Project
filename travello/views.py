from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})

"""
    dest1 = Destination()
    dest1.name = 'Medshingi'
    dest1.desc = 'The peaceful and happy village'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Bodhuuu'
    dest2.desc = 'The ok ok village of 5555 Jijuuu'
    dest2.img = 'destination_2.jpg'
    dest2.price = 100
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.desc = 'The beautiful city of The Sonuuu'
    dest3.img = 'destination_3.jpg'
    dest3.price = 500
    dest3.offer = False

    dests = [dest1, dest2, dest3]
"""
    