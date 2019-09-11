from django.shortcuts import render
from django.views import View
from .models import FilePath, Table
import csv

# Create your views here.



class TableView(View):

    def get(self, request):
        current_file = FilePath.objects.last()
        if current_file:
            required_cells = Table.objects.all()
            with open(current_file.get_path(), 'rt') as csv_file:
                headers = [cell.name for cell in required_cells]
                table = []
                table_reader = csv.DictReader(csv_file, delimiter=';')
                for table_row in table_reader:
                    row = {header: table_row[header] for header in headers}
                    table.append(row)

            result = render(request, 'table.html', {'columns': required_cells, 'table': table, 'csv_file': current_file.file_name})

            return result
