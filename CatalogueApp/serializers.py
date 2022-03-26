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
        fields = ('id', 'title', 'type', 'photo_file_name', 'time_create', 'time_update', 'price', 'height', 'width',
                  'depth', 'series', 'article', 'description', 'execution_material', 'purpose', 'tabletop_material',
                  'door_layout', 'door_quantity', 'feature', 'type_id', 'technology_rack', 'electrical_outlets',
                  'oven_material', 'lamp', 'shelf_material', 'sink_material', 'sink_location', 'boxes', 'disposition',
                  'gas', 'sink_count', 'sink_type', 'water', 'shelf_count', 'subtype_id', 'titration_panel',
                  'complete_with_drawers', 'mods')
        read_only_fields = ('time_create', 'time_update', 'price', 'mains_switch')
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
        fields = ('name', 'email', 'phone')


class OrderSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'city', 'commentary', 'price')
