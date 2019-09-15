from django.db import models

# Create your models here.


class Station(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    name = models.CharField(max_length=150, verbose_name='Название остановки')
    routes = models.ManyToManyField('Route', related_name="stations")

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'
        ordering = ['name']


class Route(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название маршрута')


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


