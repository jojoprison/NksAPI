from rest_framework import serializers
from CatalogueApp.models import Product, Type, Client, Order, Subtype, Table, Chair, Drawer, Stand, Rack, Accessory
from django.contrib.auth.models import User
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token

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


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError(detail='Пароли не совпадают!', code='password_match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.filter(user_id=instance.id).first()
        response['token'] = token.key
        return response


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)