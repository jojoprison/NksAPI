from rest_framework import serializers
from CatalogueApp.models import Product, Type, Client, Order, Subtype, Table, Chair, Drawer, Stand, Rack, Accessory


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'phone')


class OrderSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'city', 'commentary', 'price', 'delivery', 'products')


class TypeDetailSerializer(serializers.ModelSerializer):
    # TODO subtype select_related or REL

    class Meta:
        model = Type
        fields = ['id', 'title', 'subtype']

    # при добавлении нового типа (в админке, думаю поюзается)
    def validate(self, data):
        data = super().validate(data)
        title = data['title']

        if not title:
            raise serializers.ValidationError('Это поле обязательно для заполнения')

        for instance in Type.objects.all():
            if instance.name == title:
                raise serializers.ValidationError(detail="Такой тип продукта уже существует",
                                                  code="Тип продукта создан")

        return data


class SubtypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtype
        fields = '__all__'


class ReturnTitleSerializer(serializers.RelatedField):
    def to_representation(self, field_id):
        return field_id.title


class ProductListSerializer(serializers.ModelSerializer):
    # TODO мб нужно
    # rating_user = serializers.BooleanField()
    # middle_star = serializers.IntegerField()

    # type = ReturnTitleSerializer(read_only=True)
    # subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'type', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class ProductDetailSerializer(serializers.ModelSerializer):
    # type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    # type = TypeDetailSerializer(read_only=True)
    # subtype = SubtypeDetailSerializer(read_only=True)
    # TODO мб сделать так на фореин кеи, посмотреть
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    type = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')
        # exclude = ('is_published',)
        # fields = ('id', 'title', 'width', 'height', 'depth', 'countertop_material', 'disposition',
        #           'execution_material', 'purpose', 'date_added', 'photo_file_name', 'description',
        #           'slug')


class TableListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)
    
    class Meta:
        model = Table
        fields = ('id', 'title', 'type', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class TableDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Table
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')


class ChairListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)
    class Meta:
        model = Chair
        fields = ('id', 'title', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class ChairDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Chair
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')


class DrawerListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)
    class Meta:
        model = Chair
        fields = ('id', 'title', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class DrawerDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Drawer
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')


class StandListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)
    class Meta:
        model = Stand
        fields = ('id', 'title', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class StandDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Stand
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')


class RackListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Rack
        fields = ('id', 'title', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class RackDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Rack
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')


class AccessoryListSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Accessory
        fields = ('id', 'title', 'subtype', 'series', 'article', 'price',
                  'width', 'height', 'depth', 'description', 'execution_material',
                  'purpose', 'oven_material', 'tabletop_material', 'door_layout',
                  'door_quantity', 'door_material', 'boxes', 'feature', 'disposition',
                  'technology_rack', 'shelf_material', 'shelf_count', 'sink_type',
                  'sink_material', 'sink_location', 'sink_count', 'complete_with_drawers',
                  'photo_file_name',
                  # bool
                  'is_published', 'mains_switch', 'electrical_outlets', 'water',
                  'gas', 'lamp', 'titration_panel',
                  # доделать их
                  'mods')


class AccessoryDetailSerializer(serializers.ModelSerializer):
    subtype = ReturnTitleSerializer(read_only=True)

    class Meta:
        model = Accessory
        fields = '__all__'
        # TODO подумать что еще добавить в read-only
        read_only_fields = ('time_create', 'time_update')