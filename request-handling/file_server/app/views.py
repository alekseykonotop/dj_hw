from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.conf import settings

import datetime
import time
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
                'ctime': datetime.datetime.utcfromtimestamp(infostat.st_ctime),
                'mtime': datetime.datetime.utcfromtimestamp(infostat.st_mtime),
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
    filepath = f'{settings.FILES_PATH}/{name}'

    if not os.path.isfile(filepath):
        return HttpResponseNotFound(f'Файл {name} не найден')
    
    file_content = open(filepath).read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

