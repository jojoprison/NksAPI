from rest_framework import serializers
from CatalogueApp.models import Product, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'title')


class ProductSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'title', 'type', 'photo_file_name')
        # fields = ('id', 'title', 'width', 'height', 'depth', 'countertop_material', 'disposition',
        #           'execution_material', 'purpose', 'date_added', 'photo_file_name', 'description',
        #           'slug')
