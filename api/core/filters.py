import django_filters
from django_filters import rest_framework as filters
from core.models import Catalog


class CreatedDateFilter(filters.FilterSet):
    """Поля name и version уникальны только внутри одного каталога"""

    created_date_lte = django_filters.DateFilter(field_name="created_date", lookup_expr='lte')

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'version', 'short_name', 'description', 'created_date']


