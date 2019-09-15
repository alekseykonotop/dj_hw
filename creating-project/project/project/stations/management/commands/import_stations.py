from django.core.management.base import BaseCommand
from stations.models import Station, Route
import csv


class Command(BaseCommand):
    help = 'Import stations from moscow_bus_stations.csv'

    def handle(self, *args, **options):
        print('started my command')
        selected_fields = ['Latitude_WGS84', 'Longitude_WGS84', 'RouteNumbers', 'Name']

        with open('moscow_bus_stations.csv', 'rt', encoding='cp1251') as csv_file:
            print('Opened the csv-file')
            table_reader = csv.DictReader(csv_file, delimiter=';')
            for table_row in table_reader:
                new_station = Station()
                new_station.latitude = table_row[selected_fields[0]]
                new_station.longitude = table_row[selected_fields[1]]
                new_station.name = table_row[selected_fields[3]]
                new_station.save()
                routes_in_row = table_row[selected_fields[2]].split(';')
                for route in routes_in_row:
                    rt = Route.objects.get_or_create(name=route)
                    new_station.routes.add(rt[0])
                new_station.save()
