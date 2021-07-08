from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from core.filters import CreatedDateFilter
from core.models import Catalog, CatalogItem
from core.serializers import CatalogSerializer, CatalogItemSerializer, CatalogDateSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    """ Используем django-filter. Выбираем поля по которым можно фильтровать данные."""

    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'version', 'created_date']
    search_fields = ['id', 'name', 'version', 'short_name', 'description', 'created_date']
    ordering_fields = ['name', 'version', 'created_date']


class CatalogView(viewsets.ReadOnlyModelViewSet):
    """Получаем список справочников созданных ранее или ровно указанной даты"""
    filter_class = CreatedDateFilter
    queryset = Catalog.objects.all()
    serializer_class = CatalogDateSerializer


class CatalogItemViewSet(viewsets.ModelViewSet):
    """ Используем django-filter. Выбираем поля по которым можно фильтровать данные."""

    queryset = CatalogItem.objects.all()
    serializer_class = CatalogItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['catalog__name', 'catalog__version', 'catalog__created_date']
    search_fields = ['catalog__id', 'catalog__name', 'catalog__version', 'catalog__short_name', 'catalog__description',
                     'catalog__created_date', 'name_item_catalog', 'code', 'slug']
    ordering_fields = ['catalog__name', 'catalog__version', 'catalog__created_date']
