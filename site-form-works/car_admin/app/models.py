# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    review_count.short_description = 'Количество статей'


    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машины')
    title = models.CharField(max_length=100, verbose_name='Названия статей')
    text = RichTextUploadingField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'

