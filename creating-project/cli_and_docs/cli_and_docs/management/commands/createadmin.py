from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Создаем пользователя с правами администратора'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # u = User(username='unique_fellow')
        # u.set_password('a_very_cryptic_password')
        # u.is_superuser = True
        # u.is_staff = True
        # u.save()

        self.stdout.write(self.style.SUCCESS('Успешно создали админа'))

# python manage.py createadmin --name Ivanov --password 12345 --email ivanov@mail.ru