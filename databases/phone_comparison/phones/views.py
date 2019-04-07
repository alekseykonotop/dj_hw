from django.shortcuts import render
from .models import Phone, IPhone, Samsung, Xiaomi


def show_catalog(request):
    titles = {
        'brand': 'Бренд',
        'model': 'Модель',
        'memory': 'Память, Gb',
        'cost': 'Стоимость, руб.',
        'operating_system': 'Операционная система',
        'cpu': 'Процессор',
        'graphic_accelerator': 'Графический ускоритель',
        'display_size': 'Дисплей, дюймов',
        'pixels_per_inch': 'Пиксели, PPI',
        'double_camera': 'Двойная камера',
        'digital_zoom': 'Цифровой зум',
        'number_of_SIM_cards': 'Колличество сим-карт',
        'SIM_card_type': 'Тип сим-карты',
        'memory_card_support': 'Поддерживаемые карты памяти',
        'max_size_memory_card': 'Размер карты памяти, Gb',
        'A_GPS_module': 'Модуль A-GPS',
        'moisture_protection': 'Защита от брызг'
    }
    values_title_order = [value for key, value in titles.items()]
    titles_for_template = ['Наименование']
    titles_for_template.extend(values_title_order[2:])

    context_data_phones = []
    iphones = IPhone.objects.all().values()
    samsungs = Samsung.objects.all().values()
    xiaomis = Xiaomi.objects.all().values()

    for phones_set in [iphones, samsungs, xiaomis]:
        for phone in phones_set:
            phone_data = []
            phone_data.append(f'{phone["brand"]} {phone["model"]}')
            for title in list(titles.keys())[2:]:
                data = phone.get(title, '-')
                if isinstance(data, bool):
                    phone_data.append('Есть') if data else phone_data.append('Нет')
                else:
                    phone_data.append(data)
            context_data_phones.append(phone_data)

    context = {
        'titles': titles_for_template,
        'selected_phones': context_data_phones
    }


    return render(
        request,
        'catalog.html',
        context
    )

