from django import template
import time


register = template.Library()


@register.filter
def format_date(value):
    now = time.time()
    delta = now - value
    if delta // 60 < 10:
        return 'только что'

    elif delta // 3600 < 24:
        return f'{int(delta // 3600)} часов назад'

    post_date = time.localtime(value)
    return time.strftime('%Y-%m-%d', post_date)



@register.filter
def format_score(value):
    if value < -5:
        return 'все плохо'
    elif -5 <= value < 5:
        return 'нейтрально'
    else:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    elif 50 < value:
        return '50+'
    return value

@register.filter
def format_selftext(value, count):
    if not value:
        return value
    all_words = value.split(' ')
    new_str = f"{' '.join(all_words[: count])}...{' '.join(all_words[-count:])}"
    return new_str






