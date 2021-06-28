from django.contrib import admin
from .models import *


class CatalogItemTabularInline(admin.TabularInline):
    """Используем InlineModelAdmin options чтобы в админке внутри справочников отображались элементы справочника"""
    model = CatalogItem
    extra = False


class CatalogAdmin(admin.ModelAdmin):
    inlines = [CatalogItemTabularInline]

    class Meta:
        model = Catalog


admin.site.register(Catalog, CatalogAdmin)

admin.site.register(CatalogItem)


