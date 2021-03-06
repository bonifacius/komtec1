# Generated by Django 3.2.4 on 2021-06-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_versiondb_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='version',
            field=models.CharField(max_length=255, null=True, verbose_name='Версия'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='catalog',
            unique_together={('name', 'version')},
        ),
        migrations.DeleteModel(
            name='VersionDB',
        ),
    ]
