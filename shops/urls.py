
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns=[
	path("",views.geolocation, name="geo"),
	path("update_position/",views.update_position, name="update_position"),
	]
