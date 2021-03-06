# Generated by Django 3.2.4 on 2021-06-27 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя каталога')),
                ('short_name', models.CharField(max_length=255, verbose_name='Короткое имя')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('version', models.CharField(max_length=255, unique=True, verbose_name='Версия')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Справочники',
            },
        ),
    ]
