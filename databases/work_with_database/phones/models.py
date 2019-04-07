from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True, verbose_name='ID')
    name = models.TextField(verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата начала продаж')
    lte_exists = models.BooleanField(verbose_name='Наличие')
    slug = models.TextField()

    # def slug(self):
    #     return slugify(self.name)
