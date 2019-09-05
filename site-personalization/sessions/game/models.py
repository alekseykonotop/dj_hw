from django.db import models


class Player(models.Model):
    is_author = models.BooleanField(default=False, verbose_name='Автор игры')
    game_info = models.ForeignKey('PlayerGameInfo', on_delete=models.PROTECT, default=None, related_name='related_players')


    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    number = models.IntegerField(verbose_name="Загаданное число", null=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class PlayerGameInfo(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, verbose_name='Игра')
    is_active = models.BooleanField(default=False, verbose_name='Игра активна')
    attempts = models.IntegerField(default=0, verbose_name='Колличество попыток')

    class Meta:
        verbose_name = 'Инфо об игре'
        verbose_name_plural = 'Инфа об играх'
        ordering = ['game']
