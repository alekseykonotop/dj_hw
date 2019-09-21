from django.db import models
from django.conf import settings

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название поля')
    width = models.IntegerField(verbose_name='Ширина поля')
    serial_number = models.IntegerField(verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'
        ordering = ['serial_number', ]


class FilePath(models.Model):
    file_name = models.CharField(max_length=150, verbose_name='Имя файла', default='')
    folder_name = models.CharField(max_length=100, verbose_name='Имя папки для хранения', default='')
    is_selected = models.BooleanField(verbose_name='Файл выбран', default=False)


    class Meta:
        verbose_name = 'Путь до файла'
        verbose_name_plural = 'Пути до файлов'

    def get_path(self):
        """Получаем полный путь до файла
        """
        return f'{self.folder_name}/{self.file_name}'

