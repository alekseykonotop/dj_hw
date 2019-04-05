from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from django.core.paginator import Paginator
from django.conf import settings
import urllib.parse
import csv


def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    current_page = int(request.GET.get('page', 1))

    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Class Paginator
        p = Paginator(list(reader), 10)
        data_on_page = p.page(current_page).object_list

    # next page
    next_page = current_page + 1 if p.page(current_page).has_next() else None
    next_params = urllib.parse.urlencode({'page': next_page})

    # prev page
    prev_page = current_page - 1 if p.page(current_page).has_previous() else None
    prev_params = urllib.parse.urlencode({'page': prev_page}) if prev_page else ''

    return render_to_response('index.html', context={
        'bus_stations': data_on_page,
        'current_page': current_page,
        'prev_page_url': f'bus_stations?{prev_params}' if prev_page else None,
        'next_page_url': f'bus_stations?{next_params}' if next_page else None,
    })

