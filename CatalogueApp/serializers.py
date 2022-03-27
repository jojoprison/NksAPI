from rest_framework import serializers
from CatalogueApp.models import Product, Type, Client, Order, Subtype


class TypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class SubtypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtype
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    # TODO мб нужно
    # rating_user = serializers.BooleanField()
    # middle_star = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'type', 'subtype', 'series', 'article', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    # type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    type = TypeDetailSerializer(read_only=True)
    subtype = SubtypeDetailSerializer(read_only=True)
    # TODO мб сделать так на фореин кеи, посмотреть
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')
        # exclude = ("draft",)
        # fields = ('id', 'title', 'width', 'height', 'depth', 'countertop_material', 'disposition',
        #           'execution_material', 'purpose', 'date_added', 'photo_file_name', 'description',
        #           'slug')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'phone')


class OrderSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'city', 'commentary', 'price')
