import datetime
import time

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH
import os


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files_list = os.listdir(FILES_PATH)
        if not files_list:
            return

        file_objects_list = []
        for f in files_list:
            infostat = os.stat(f'{FILES_PATH}/{f}')
            if not date:
                file_objects_list += [self.create_file_object(f, infostat)]
            else:
                year, month, day = map(int, self.url_converter(date))
                search_date = datetime.date(year, month, day)
                file_creation_time = datetime.datetime.utcfromtimestamp(infostat[-1])
                file_objects_list += [self.create_file_object(f, infostat)] if file_creation_time.date() == search_date else []
        file_objects_list.reverse()
        return {
            'files': file_objects_list,
            'date': datetime.date(year, month, day) if date else ''
        }

    def create_file_object(self, file_name, f_stat):
        return {
            'name': file_name,
            'ctime': datetime.datetime.utcfromtimestamp(f_stat[-1]),
            'mtime': datetime.datetime.utcfromtimestamp(f_stat[-2])
        }

    def url_converter(self, url_tail):
        return url_tail.split('-')


def file_content(request, name):
    file_content = open(f'{FILES_PATH}/{name}').read()
    return render(
        request,
        'file_content.html',
        context={'file_name': f'{name}', 'file_content': f'{file_content}'}
    )

