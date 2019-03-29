from django.urls import path

from app.views import index, bus_stations
import re


urlpatterns = [
    path('', index, name='index'),
    path('bus_stations', bus_stations, name='bus_stations'),
]
