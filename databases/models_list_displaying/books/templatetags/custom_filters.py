
from django import template


register = template.Library()


@register.filter
def create_slug(value):
    slug_date = value.strftime('%Y-%m-%d')
    return slug_date

@register.filter
def human_date(value):
    return value.strftime('%Y.%m.%d')