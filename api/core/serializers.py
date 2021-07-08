from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from core.models import Catalog, CatalogItem


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Catalog.objects.all(),
                fields=['name', 'version']
            )
        ]


class CatalogItemSerializer(ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=CatalogItem.objects.all(),
                fields=['code', 'name_item_catalog']
            )
        ]


class CatalogDateSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
