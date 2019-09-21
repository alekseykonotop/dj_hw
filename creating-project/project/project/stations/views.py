from django.shortcuts import render
from .models import Route
from django.db.models import Min, Max

# Create your views here.


def stations(request):
    context = {}
    all_routes = Route.objects.all()
    routes_for_template = [r.name for r in all_routes]
    context['routes'] = routes_for_template
    requested_route = request.GET.get('route')
    if not requested_route:
        center = {'y': 55.75429177,
                  'x': 37.62300867}
        context['center'] = center
        context['zoom'] = 11

        return render(request, 'stations.html', context)

    actual_route = Route.objects.get(name=requested_route)
    stations_on_route = actual_route.stations.all()
    context['stations'] = stations_on_route

    coord_max_min = stations_on_route.aggregate(Min('latitude'), Max('latitude'),
                                                Min('longitude'), Max('longitude'))
    latitude_min = coord_max_min['latitude__min']
    latitude_max = coord_max_min['latitude__max']
    longitude_min = coord_max_min['longitude__min']
    longitude_max = coord_max_min['longitude__max']

    middle_latitude = latitude_max - (latitude_max - latitude_min) / 2
    middle_longitude = longitude_max - (longitude_max - longitude_min) / 2
    center = {'x': round(middle_longitude, 2),
              'y': round(middle_latitude, 2)}

    context['zoom'] = 13
    context['center'] = center

    return render(request, 'stations.html', context)
