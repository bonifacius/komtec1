# Generated by Django 3.2.4 on 2021-06-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_versiondb_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versiondb',
            name='version',
            field=models.CharField(max_length=255, verbose_name='Версия'),
        ),
    ]
