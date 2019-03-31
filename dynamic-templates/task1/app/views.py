from django.shortcuts import render
from django.views.generic import TemplateView
from app.settings import BASE_DIR

import csv


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        table_titles = ['Год', ' Январь', 'Февраль', 'Март',
                        'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Всего']
        ready_titles = self.prepare_titles(table_titles)

        with open(f'{BASE_DIR}/inflation_russia.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            inflation_data = list(reader)
            correct_data = [[data if data else '-' for data in data_row] for data_row in inflation_data[1:]]
            ready_data = [self.prepare__inflation_data(row) for row in correct_data]
            context = {
                'titles': ready_titles,
                'years_data': ready_data
            }

        # print(f'context ===> {context}')

        return render(request, self.template_name, context)

    def prepare_titles(self, titles):
        colors = {
            'white': '#FFFFFF',
            'gray': '#808080',
        }

        prepared_data = []
        for i in range(len(titles)):
            if i != len(titles) - 1:
                color_type = 'white'
            else:
                color_type = 'gray'

            single_data = {
                'value': titles[i],
                'color': colors[color_type]
            }
            prepared_data += [single_data]

        return prepared_data


    def prepare__inflation_data(self, data_list):
        """
        Принимает список.
        Подготавливает данные по каждому значению инфляции
        в формате {'value': 0.35, 'color': '#FFFFFF'}.
        """

        colors = {
            'white': '#FFFFFF',
            'dark_red': '#8B0000',
            'red': '#FF0000',
            'light_red': '#F08080',
            'gray': '#808080',
            'green': '#227F00'
        }

        prepared_data = []
        print(f'len ==> {len(data_list)}')
        for i in range(len(data_list)):
            if i == 0:
                color_type = 'white'

            elif 0 < i < len(data_list) - 1:
                if data_list[i] == '-':
                    color_type = 'white'
                elif float(data_list[i]) < 0:
                    color_type = 'green'
                elif 0 < float(data_list[i]) < 1:
                    color_type = 'white'
                elif 1 <= float(data_list[i]) < 2:
                    color_type = 'light_red'
                elif 2 <= float(data_list[i]) < 5:
                    color_type = 'red'
                elif 5 <= float(data_list[i]):
                    color_type = 'dark_red'
            elif i == len(data_list) - 1:
                color_type = 'gray'

            single_data = {
                'value': data_list[i],
                'color': colors[color_type]
            }
            prepared_data += [single_data]

        return prepared_data