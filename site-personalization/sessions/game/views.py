from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo
from .forms import GuessNumberForm


def show_home(request):
    context = {}

    if request.method == 'POST':
        if request.session['is_author']:
            form = GuessNumberForm(request.POST or None)
            if form.is_valid():
                author_number = form.cleaned_data.get('number')
                game = Game.objects.get(pk=request.session['game_id'])
                game.number = author_number
                game.save()

                context['message'] = f'Загаданное число: {game.number}'
                context['descriptor'] = 'Второй игрок будет пытаться отгадать его'

        else:
            form = GuessNumberForm(request.POST or None)
            if form.is_valid():
                guess_number = form.cleaned_data.get('number')
                current_game = Game.objects.get(pk=request.session['game_id'])
                actual_number = current_game.number  # Загаданное автором игры число
                pg_info = Player.objects.get(pk=request.session['player_id']).game_info
                pg_info.attempts += 1
                pg_info.save()

                if guess_number < actual_number:
                    context['message'] = 'Загаданное число больше! Попробуйте еще раз.'
                    context['form'] = GuessNumberForm()
                elif guess_number > actual_number:
                    context['message'] = 'Загаданное число меньше! Попробуйте еще раз.'
                    context['form'] = GuessNumberForm()
                elif guess_number == actual_number:
                    context['message'] = f'Вы угадали число с {pg_info.attempts} попытки'
                    pg_info.is_active = False
                    pg_info.save()
                    request.session.flush()

    elif request.method == 'GET':
        if 'game_id' in request.session:  # Уже играет в игру
            current_game = Game.objects.get(pk=request.session['game_id'])
            is_game_active = current_game.playergameinfo.is_active  # Is game active or not
            if not is_game_active:  # Нет активной игры - угадали

                if request.session['is_author']:
                    context['message'] = f'Загаданное число {current_game.number}'
                    context['descriptor'] = f'Ваше число отгадали с {current_game.playergameinfo.attempts} попытки'
                    request.session.flush()
            else:
                if request.session['is_author']:
                    context['message'] = f'Загаданное число {current_game.number}'
                    context['descriptor'] = f'Второй игрок еще пытается отгадать ваше число'

                else:
                    context['message'] = 'Вам надо отгадать число!'
                    context['form'] = GuessNumberForm()
        else:
            if not PlayerGameInfo.objects.filter(is_active=True).exists():
                game = Game.objects.create()
                game.save()
                request.session['game_id'] = game.pk
                p_g_info = PlayerGameInfo(game=game, is_active=True)
                p_g_info.save()

                player = Player.objects.create(is_author=True, game_info=p_g_info)
                player.save()

                context['message'] = 'Вы - автор игры. Загадайте число'

            else:
                game_info = PlayerGameInfo.objects.get(is_active=True)
                player = Player.objects.create(is_author=False, game_info=game_info)
                player.save()
                context['message'] = 'Вам надо отгадать число!'
                game_id = game_info.game.pk
                request.session['game_id'] = game_id

            player.save()
            request.session['player_id'] = player.pk
            request.session['is_author'] = player.is_author
            context['form'] = GuessNumberForm()

    return render(
        request,
        'home.html',
        context
    )
