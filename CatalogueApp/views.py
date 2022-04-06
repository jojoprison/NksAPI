import json
import operator
from functools import reduce

from django.contrib.gis.measure import D
from django.db.models import Q, BooleanField, F, CharField, JSONField
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response

from CatalogueApp.models import Product, Type, Client, Table, Chair, Drawer, Stand, Rack, Accessory, Order
from CatalogueApp.serializers import (
    TypeDetailSerializer,
    SubtypeDetailSerializer,
    OrderSerializer,
    ClientSerializer, ProductListSerializer, ProductDetailSerializer, TableListSerializer, TableDetailSerializer,
    ChairListSerializer, ChairDetailSerializer, DrawerListSerializer, DrawerDetailSerializer, StandDetailSerializer,
    StandListSerializer, RackListSerializer, RackDetailSerializer, AccessoryListSerializer, AccessoryDetailSerializer
)

from django.core.files.storage import default_storage

from common.utils.whatsapp_notifications import WhatsAppNotificator
from .service import ProductFilter, get_client_ip, ProductsPagination, TableFilter, ChairFilter, DrawerFilter, \
    StandFilter, RackFilter, AccessoryFilter


# ModelViewSet
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        # radius = self.request.query_params.get('radius')

        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'type':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                products = Product.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                products = Product.objects.all()

            return products

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Product.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TableFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                tables = Table.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                tables = Table.objects.all()

            return tables

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Table.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return TableListSerializer
        elif self.action == 'retrieve':
            return TableDetailSerializer

    # добавляет новый маршрут во view_set
    # @action(methods=['get'], detail=True)
    # def type(self, request, pk=None):
    #     type = Type.objects.get(pk=pk)
    #     return Response({'type_id': type.id})


class ChairViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChairFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                chair = Chair.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                chair = Chair.objects.all()

            return chair

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Chair.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return ChairListSerializer
        elif self.action == 'retrieve':
            return ChairDetailSerializer


class DrawerViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DrawerFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                drawer = Drawer.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                drawer = Drawer.objects.all()

            return drawer

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Chair.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return DrawerListSerializer
        elif self.action == 'retrieve':
            return DrawerDetailSerializer


class StandViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StandFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                stand = Stand.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                stand = Stand.objects.all()

            return stand

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Stand.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return StandListSerializer
        elif self.action == 'retrieve':
            return StandDetailSerializer


class RackViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RackFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                rack = Rack.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                rack = Rack.objects.all()

            return rack

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Rack.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return RackListSerializer
        elif self.action == 'retrieve':
            return RackDetailSerializer


class AccessoryViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccessoryFilter
    pagination_class = ProductsPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'subtype':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                accessory = Accessory.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                accessory = Accessory.objects.all()

            return accessory

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Accessory.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return AccessoryListSerializer
        elif self.action == 'retrieve':
            return AccessoryDetailSerializer


@csrf_exempt
def product_api(request, product_id=0):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductDetailSerializer(products, many=True)

        return JsonResponse(product_serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductDetailSerializer(data=product_data)

        if product_serializer.is_valid():
            product_serializer.save()

            return JsonResponse('Product Added', safe=False)

        return JsonResponse('Product Failed to Add', safe=False)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)

        product = Product.objects.get(id=product_data['id'])
        product_serializer = ProductDetailSerializer(product, data=product_data)

        if product_serializer.is_valid():
            product_serializer.save()

            return JsonResponse('Product Updated', safe=False)

        return JsonResponse('Failed to Update', safe=False)

    elif request.method == 'DELETE':
        product = Product.objects.get(id=product_id)
        product.delete()

        return JsonResponse('Product Deleted', safe=False)


@csrf_exempt
def product_detail_api(request, product_id):
    print(product_id)
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        product_serializer = ProductDetailSerializer(product)

        return JsonResponse(product_serializer.data, safe=False)


def product_filter_all_api(request):
    if request.method == 'GET':
        published_products = Product.objects.all()
        print(len(published_products))

        # photo_list = list(set(published_products.values_list('photo_file_name', flat=True)))
        # TODO не сортируется потому что у некоторых товаров ссылки на картинки вместо фоток
        # photo_list.sort()
        # print(len(photo_list))

        # price_list = Product.objects.order_by('price').values_list('price', flat=True).distinct()
        #     # list(set(published_products.exclude(price=None).values_list('price', flat=True)))
        # # print(price_list)
        # price_list.sort()

        fields = [f for f in Product._meta.fields]
        select_list = []
        checkbox_list = []
        for field in fields:
            # queries.append(Q(**{field.name: SEARCH_TERM}))
            excluded = ['description', 'time_create', 'time_update', 'photo_file_name', 'article', 'is_published', 'id',
                        'title', 'subtype', 'price', 'mods']
            # json_fields = ['features', 'door_layout', 'shelf_material', 'complete_with_drawers', 'mods', ]

            field_name = field.name

            if field_name not in excluded:
                if isinstance(field, BooleanField):
                    checkbox_list.append(field.name)
                else:
                    excludes = None

                    if isinstance(field, JSONField):
                        # TODO не доделал
                        empty_q = Q(**{f'{field_name}__exact': '[]'})
                        excludes = (excludes and (excludes | empty_q)) or empty_q

                        # TODO на фронте делать мультиселект для таких полей
                    else:
                        excludes = None

                        null_q = Q(**{f'{field_name}__isnull': True})
                        # makes sure excludes is set properly
                        excludes = (excludes and (excludes | null_q)) or null_q
                        if isinstance(field, CharField):
                            empty_q = Q(**{f'{field_name}__exact': ''})
                            excludes = (excludes and (excludes | empty_q)) or empty_q

                        pre_excluded_values = Product.objects.order_by(field_name).values_list(field_name, flat=True) \
                            .distinct()
                        values_minus_excluded = pre_excluded_values.exclude(excludes)
                        values = list(values_minus_excluded)

                        if field_name == 'features':
                            print(values)

                        if values:
                            select = {'product_prop': field.name,
                                      'name': field.verbose_name,
                                      'values': values}
                            select_list.append(select)

        # print(select_list)


        # qs = Q()
        # for query in queries:
        #     qs = qs | query
        #
        # Product.objects.filter(qs)

        # width_list = list(set(published_products.exclude(width=None).values_list('width', flat=True)))
        # width_list.sort()
        #
        # height_list = list(set(published_products.exclude(height=None).values_list('height', flat=True)))
        # height_list.sort()
        #
        #
        # type_list = list(set(published_products.values_list('type', flat=True)))
        # type_list.sort()
        # print(type_list)
        # print(res)


        filter_variant_list = {
            'select': select_list,
            'checkbox': checkbox_list
        }

        # print(filter_variant_list)

        return JsonResponse(filter_variant_list, safe=False)


def product_filter_api(request):
    if request.method == 'GET':
        filter_kwargs = []

        # qs = Q()
        # for query in queries:
        #     qs = qs | query

        for item in request.GET.items():
            # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
            if item[0] == 'type':
                filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
            else:
                filter_kwargs.append(Q(**{item[0]: item[1]}))

        # TODO выводим все (не только опубликованные)
        # filter_kwargs.append(Q(**{'is_published': True}))
        # print(filter_kwargs)

        # TODO заменить проверки вот тут
        if request.GET.get('photo', None) == 'ALL':
            products = Product.objects.all()
        else:
            if filter_kwargs:
                products = Product.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                products = Product.objects.all()

        # print(products)

        product_serializer = ProductDetailSerializer(products, many=True)

        return JsonResponse(product_serializer.data, safe=False)


@csrf_exempt
def type_api(request, type_id=0):
    if request.method == 'GET':
        types = Type.objects.all()
        type_serializer = TypeDetailSerializer(types, many=True)

        return JsonResponse(type_serializer.data, safe=False)

    elif request.method == 'POST':
        type_data = JSONParser().parse(request)
        type_serializer = TypeDetailSerializer(data=type_data)

        if type_serializer.is_valid():
            type_serializer.save()

            return JsonResponse('Type Added', safe=False)

        return JsonResponse('Type Failed to Add', safe=False)

    elif request.method == 'PUT':
        type_data = JSONParser().parse(request)

        type_ = Type.objects.get(id=type_data['id'])
        type_serializer = TypeDetailSerializer(type_, data=type_data)

        if type_serializer.is_valid():
            type_serializer.save()

            return JsonResponse('Type Updated', safe=False)

        return JsonResponse('Type to Update', safe=False)

    elif request.method == 'DELETE':
        type_ = Type.objects.get(id=type_id)
        type_.delete()

        return JsonResponse('Type Deleted', safe=False)


@csrf_exempt
def client_api(request):
    if request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)

        if client_serializer.is_valid():
            client_serializer.save()

        return JsonResponse('Client Added', safe=False)


@csrf_exempt
def order_api(request):
    if request.method == 'POST':
        order_data = JSONParser().parse(request)

        items = order_data.get('items')
        products_db = []

        for item in items:
            item_id = item.get('id')
            title = item.get('title')
            item_quantity = item.get('quantity')
            item_price = item.get('price')


            # 23:04 пример СМС
            # product = {'ID товара': item_id,
            #            'Название товара': title,
            #            'Количество': item_quantity,
            #            'Цена': item_price}

            # 23:23 пример СМС
            product = (f' ID товара: {item_id},'
                       f' Название товара: {title},'
                       f' Количество: {item_quantity},'
                       f' Цена: {item_price}')
            products_db.append(product)

        order_data.pop('items')
        # print(products_db)
        products_db_str = json.dumps(products_db)
        order_data['products'] = products_db_str

        # print(products_db_str)

        # TODO сделать парсер чтоб приводить телефон к общему виду
        # order_client_phone = order_data.pop('phone')
        # order_client_email = order_data.pop('email')
        # client = None

        # if order_client_phone or order_client_email:
        #     client = Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).first()
        #     print(Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).query)
        #
        # order_data['client'] = client.id
        # order_name = order_data['name']


        order_serializer = OrderSerializer(data=order_data)


        if order_serializer.is_valid():
            saved_order = order_serializer.save()

            delivery = order_data['delivery']
            total_price = order_data['price']
            client = order_data['name']
            number_phone = order_data['phone']
            # products = order_data['products']


            order_message = (f'Заказ №{saved_order.id}.\nФИО клиента: {client}.\nТелефон для связи: {number_phone}.\n'
                                               f'Сумма заказа: {total_price} ₽.\nСпособ доставки: {delivery}.\n'
                                               f'Товары: {products_db}')

            WhatsAppNotificator().send_message(order_message)

            return JsonResponse('Заказ оформлен', safe=False)

        return JsonResponse('Не удалось оформить заказ', safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['myFile']
    file_name = default_storage.save('products/' + file.name, file)

    return JsonResponse(file_name, safe=False)
