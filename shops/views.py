
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from.models import Position
from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
longitude = 83.4091463
latitude = 28.018795

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "shops/index.html"


home = Home.as_view()

def geolocation(request):
	return render(request, "shops/getlocation.html")
	

def update_position(request):
	if request.method == 'POST':
		lat=request.POST['lat']
		lon=request.POST['lon']
		print(type(lat))
		print(type(lon))
		latitude=Decimal(lat)
		longitude=Decimal(lon)
		location=Point(latitude,longitude,srid=4326)

		Position.objects.create(latitude=lat,
			longitude=lon
			)
		print(latitude)
		
	
		
		return HttpResponse("update sucessful")
	else:
		return HttpResponse("update not sucessful")



	