from django.shortcuts import render
from .models import Station, Route
from django.db.models import Min, Max

# Create your views here.


class Point(object):
    """
    Creates a point on a coordinate
    plane with values x and y.
    """

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y



def stations(request):
    context = {}

    # 1. Получить все записи маршрутов
    all_routes = Route.objects.all()
    route_names = [r.name for r in all_routes]
    context['routes'] = route_names

    # Получить данные по остановкам выбранного маршрута
    requested_route = request.GET.get('route')  # type string
    print(f'Передали параметром маршрут: {requested_route}')
    if requested_route:

        # 1. Получаем объект записи переданного маршрута
        actual_route = Route.objects.get(name=requested_route)
        stations_on_route = actual_route.stations.all()
        context['stations'] = stations_on_route

        # 2. Координаты центра отображаемой карты
        latitude_result = Station.objects.aggregate(Min('latitude'), Max('latitude'))
        latitude_min = latitude_result['latitude__min']
        latitude_max = latitude_result['latitude__max']
        print(f'Узнали мин и макс широты: min= {latitude_min}, max= {latitude_max}')

        longitude_result = Station.objects.aggregate(Min('longitude'), Max('longitude'))
        longitude_min = longitude_result['longitude__min']
        longitude_max = longitude_result['longitude__max']
        print(f'Узнали мин и макс долготы: min= {longitude_min}, max= {longitude_max}')

        # 3. Расчитываем координаты средней точки
        middle_latitude = latitude_max - (latitude_max - latitude_min) / 2
        middle_longitude = longitude_max - (longitude_max - longitude_min) / 2
        # print(f'middle point is: latitude= {middle_latitude}, longitude= {middle_longitude}')
        # Создаем экземпляр класса Point с координатам middle station
        # center = Point(middle_latitude, middle_longitude)
        center = {'x': round(middle_longitude, 2),
                  'y': round(middle_latitude, 2)}
        print(f'center= {center}')
        context['center'] = center

    return render(request, 'stations.html', context)
