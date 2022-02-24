from rest_framework import serializers
from CatalogueApp.models import Product, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('title',)
        # TODO написать свой валидарот для тайтла из-за unique
        extra_kwargs = {
            'title': {
                'validators': [],
            }
        }

    # def validate_title(self, title):
    #     if 'django' not in title.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return title


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Product
        fields = ('title', 'type')
        # fields = ('id', 'title', 'width', 'height', 'depth', 'countertop_material', 'disposition',
        #           'execution_material', 'purpose', 'date_added', 'photo_file_name', 'description',
        #           'slug')

    def create(self, validated_data):
        type_data = validated_data.pop('type')

        product_type = Type.objects.get_or_create(title=type_data['title'])

        product = Product.objects.create(type=product_type[0], **validated_data)

        return product


