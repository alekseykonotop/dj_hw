# Generated by Django 2.2 on 2019-09-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20190911_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepath',
            name='folder_name',
            field=models.CharField(default='', max_length=100, verbose_name='Имя папки для хранения'),
        ),
    ]
