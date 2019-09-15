from django.shortcuts import render
from .models import Station

# Create your views here.
def station(request):
    print('Проверим сколько записей station имеем в БД ')
    count_writes_in_model = Station.objects.count()
    print(f'Всего в БД ==>{count_writes_in_model}<== записей')
    return render(request, 'stations.html')
