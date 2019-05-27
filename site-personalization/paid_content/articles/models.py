from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    subscription = models.BooleanField(verbose_name='Подписка')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['user']


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Текст')
    is_paid_content = models.BooleanField(verbose_name='Входит в платную подписку')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']
