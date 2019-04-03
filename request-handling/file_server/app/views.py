import datetime
import time

from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings
# from app.settings import FILES_PATH
import os


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files_list = os.listdir(settings.FILES_PATH)
        if not files_list:
            return

        file_objects_list = []
        for f in files_list:
            infostat = os.stat(f'{settings.FILES_PATH}/{f}')
            f_data = {
                'name': f,
                'ctime': datetime.datetime.utcfromtimestamp(infostat[-1]),
                'mtime': datetime.datetime.utcfromtimestamp(infostat[-2])
            }

            if not date:
                file_objects_list += [f_data]
            else:
                year, month, day, *_ = time.strptime(date, "%Y-%m-%d")
                search_date = datetime.date(year, month, day)
                file_creation_time = datetime.datetime.utcfromtimestamp(infostat[-1])
                
                file_objects_list += [f_data] if file_creation_time.date() == search_date else []
        file_objects_list.reverse()
        
        return {
            'files': file_objects_list,
            'date': datetime.date(year, month, day) if date else ''
        }


def file_content(request, name):
    file_content = open(f'{settings.FILES_PATH}/{name}').read()
    return render(
        request,
        'file_content.html',
        context={'file_name': f'{name}', 'file_content': f'{file_content}'}
    )

