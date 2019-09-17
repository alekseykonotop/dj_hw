from django.core.management.base import BaseCommand
from stations.models import Station, Route
import csv


class Command(BaseCommand):
    help = 'Import stations from moscow_bus_stations.csv'

    def handle(self, *args, **options):
        print('Start my management command')
        selected_fields = ['Latitude_WGS84', 'Longitude_WGS84', 'RouteNumbers', 'Name']

        with open('moscow_bus_stations.csv', 'rt', encoding='cp1251') as csv_file:
            print('Opened the csv-file')
            table_reader = csv.DictReader(csv_file, delimiter=';')
            print('Start import')
            for table_row in table_reader:
                new_station = Station()
                try:
                    new_station.latitude = float(table_row[selected_fields[0]])
                except ValueError:
                    continue
                try:
                    new_station.longitude = float(table_row[selected_fields[1]])
                except ValueError:
                    continue
                new_station.name = table_row[selected_fields[3]]
                new_station.save()
                routes_in_row = table_row[selected_fields[2]].split(';')
                for route in routes_in_row:
                    route = route.replace(' ', '')
                    rt, _ = Route.objects.get_or_create(name=route)
                    new_station.routes.add(rt)
                    new_station.save()
            print('Import completed')
