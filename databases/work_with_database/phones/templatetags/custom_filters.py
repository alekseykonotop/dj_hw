from datetime import datetime
from django import template


register = template.Library()


@register.filter
def accurate_date(value):
    accurate_date = value.strftime('%Y.%m.%d')
    return accurate_date


@register.filter
def yes_or_no(value):
    if value:
        return 'Есть'
    else:
        return 'Нет'