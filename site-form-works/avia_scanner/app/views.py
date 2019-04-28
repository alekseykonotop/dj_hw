from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache
from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term')
    if not cache.has_key('cities'):
        cache.set('cities', City.objects.order_by('name'))
    results = [city.name for city in cache.get('cities') if term in city.name]

    return JsonResponse(results, safe=False)
