from rest_framework import serializers
from CatalogueApp.models import Product, Type, Client, Order


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'title')


class ProductSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'title', 'type', 'photo_file_name', 'time_create', 'time_update', 'price')
        read_only_fields = ('time_create', 'time_update', 'price')
        # fields = ('id', 'title', 'width', 'height', 'depth', 'countertop_material', 'disposition',
        #           'execution_material', 'purpose', 'date_added', 'photo_file_name', 'description',
        #           'slug')


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('photo_file_name',)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'phone_number')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model: Order
        fields = ('__all__',)