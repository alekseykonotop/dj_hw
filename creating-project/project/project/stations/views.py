from django.shortcuts import render
from .models import Station, Route

# Create your views here.
def stations(request):
    context = {}

    # 1. Получить все записи маршрутов
    all_routes = Route.objects.all()
    route_names = [r.name for r in all_routes]
    context['routes'] = route_names

    # Получить данные по остановкам выбранного маршрута
    requested_route = request.GET.get('route')
    if requested_route:
        pass

    # координаты центра отображаемой карты,


    return render(request, 'stations.html')
