from rest_framework.serializers import ModelSerializer

from core.models import Catalog, CatalogItem


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class CatalogItemSerializer(ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = '__all__'


class CatalogDateSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
