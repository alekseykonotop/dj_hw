# Generated by Django 2.2 on 2019-04-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190414_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compilation',
            options={'ordering': ['-is_main'], 'verbose_name': 'Связь', 'verbose_name_plural': 'Связи'},
        ),
    ]
