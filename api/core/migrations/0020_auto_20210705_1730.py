# Generated by Django 3.2.4 on 2021-07-05 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_catalogitem_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='catalogitem',
            name='slug',
        ),
    ]