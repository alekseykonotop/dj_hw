from django.shortcuts import render
from .models import Phone
from .management.commands.import_phones import Command


def show_catalog(request):
    sort = request.GET.get('sort')
    record_data_to_db = Command()
    record_data_to_db.handle()

    if not sort:
        phones = Phone.objects.all().values()
    elif sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')

    context = {
        'phones': phones,
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    phone_name = slug.replace('-', ' ')
    search_name = phone_name.title()
    requested_set = Phone.objects.filter(name=search_name)
    actual_phone = requested_set[0]

    context = {
        'phone': actual_phone
    }

    return render(
        request,
        'product.html',
        context
    )
