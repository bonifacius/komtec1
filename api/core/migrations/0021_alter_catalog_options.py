# Generated by Django 3.2.4 on 2021-07-06 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210705_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
    ]