import django_filters
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Type, Table, Chair, Drawer, Stand, Rack, Accessory


class ProductsPagination(PageNumberPagination):
    page_size = 12
    # max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'product_count': self.page.paginator.count,
            'per_page': self.page_size,
            'page_count': self.page.paginator.num_pages,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data
        })


class NumberFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class EmptyStringPlugFilter(filters.CharFilter):
    empty_value = 'EMPTY'

    def filter(self, qs, value):
        if value != self.empty_value:
            return super().filter(qs, value)

        qs = self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): ""})
        return qs.distinct() if self.distinct else qs


class EmptyValueStringFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value in [None, 'Не указано', 'Не задано', 'Любое', 'Пустое']:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.field_name: ""})

# пример если хотим так на пустоту првоерять
# class MyFilterSet(filters.FilterSet):
#     myfield__isempty = EmptyValueStringFilter(field_name='myfield')
#
#     class Meta:
#         model = MyModel
#         fields = []


class ProductFilter(filters.FilterSet):
    # type = NumberFilterInFilter(field_name='type_id', lookup_expr='in')

    # type = django_filters.ModelChoiceFilter(
    #     field_name='type', lookup_expr='isnull',
    #     null_label='Без типа',
    #     queryset=Type.objects.all(),
    # )

    class Meta:
        model = Product
        fields = ['type', 'series', 'subtype']


class TableFilter(filters.FilterSet):
    class Meta:
        model = Table
        fields = ['series', 'subtype']


class ChairFilter(filters.FilterSet):
    class Meta:
        model = Chair
        fields = ['series', 'subtype']


class DrawerFilter(filters.FilterSet):
    class Meta:
        model = Drawer
        fields = ['series', 'subtype']


class StandFilter(filters.FilterSet):
    class Meta:
        model = Stand
        fields = ['series', 'subtype']


class RackFilter(filters.FilterSet):
    class Meta:
        model = Rack
        fields = ['series', 'subtype']


class AccessoryFilter(filters.FilterSet):
    class Meta:
        model = Accessory
        fields = ['series', 'subtype']


def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



