from django.db import models
from django.utils import timezone


class Catalog(models.Model):
    name = models.CharField('Имя каталога', max_length=255)
    short_name = models.CharField('Короткое имя', max_length=255)
    description = models.CharField('Описание', max_length=255)
    version = models.CharField('Версия', max_length=255, null=True)
    created_date = models.DateField('Дата создания', default=timezone.now)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return 'Имя: {} Версия: {}'.format(self.name, self.version)

    class Meta:
        """Поля name и version уникальны только внутри одного каталога"""
        unique_together = ['name', 'version']
        ordering = ['-version']
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


class CatalogItem(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    code = models.CharField('Код элемента', max_length=255)
    name_item_catalog = models.CharField('Значение элемента', max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return 'Имя: {} Версия:{} Элемент:{}'.format(Catalog.name, Catalog.version, self.name_item_catalog)

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'
