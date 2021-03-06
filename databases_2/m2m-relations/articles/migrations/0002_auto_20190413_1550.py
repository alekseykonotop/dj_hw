# Generated by Django 2.2 on 2019-04-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['published_at', '-title']},
        ),
        migrations.AlterField(
            model_name='compilation',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Статьи'),
        ),
    ]
