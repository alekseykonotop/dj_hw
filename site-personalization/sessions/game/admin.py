from django.contrib import admin
from .models import Game, Player, PlayerGameInfo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('is_author', )


class GameAdmin(admin.ModelAdmin):
    list_display = ('number', )


class PlayerGameInfoAdmin(admin.ModelAdmin):
    list_display = ('game', 'is_active', 'attempts')


admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)
