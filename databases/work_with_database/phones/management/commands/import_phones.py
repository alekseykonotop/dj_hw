import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            # phone_reader = csv.reader(csvfile, delimiter=';')
            # # пропускаем заголовок
            # next(phone_reader)
            #
            # for line in phone_reader:
            #     # TODO: Добавьте сохранение модели
            #     pass

            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                phone_data = Phone()
                phone_data.id = row['id']
                phone_data.name = row['name']
                phone_data.price = row['price']
                phone_data.image = row['image']
                phone_data.release_date = row['release_date']
                phone_data.lte_exists = row['lte_exists']
                phone_data.slug = slugify(phone_data.name)
                phone_data.save()


