import json
import operator
from functools import reduce

from django.contrib.gis.measure import D
from django.db.models import Q, BooleanField
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response

from CatalogueApp.models import Product, Type, Client
from CatalogueApp.serializers import (
    TypeDetailSerializer,
    SubtypeDetailSerializer,
    OrderSerializer,
    ClientSerializer, ProductListSerializer, ProductDetailSerializer
)

from django.core.files.storage import default_storage


from .service import ProductFilter, get_client_ip, PaginationProducts


# ModelViewSet
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = PaginationProducts

    def get_queryset(self):
        # longitude = self.request.query_params.get('longitude')
        # latitude = self.request.query_params.get('latitude')
        # radius = self.request.query_params.get('radius')

        pk = self.kwargs.get('pk')

        if not pk:
            return Product.objects.all()

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Product.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer

    # добавляет новый маршрут во view_set
    # @action(methods=['get'], detail=True)
    # def type(self, request, pk=None):
    #     type = Type.objects.get(pk=pk)
    #     return Response({'type_id': type.id})


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

        photo_list = list(set(published_products.values_list('photo_file_name', flat=True)))
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
                        'title', 'type', 'subtype', 'oven_material', 'door_material']
            if field.name not in excluded:
                if not isinstance(field, BooleanField):
                    values = list(Product.objects.order_by(field.name).values_list(field.name, flat=True).distinct())
                    select = {'product_prop': field.name,
                              'name': field.verbose_name,
                              'values': values}
                    select_list.append(select)
                else:
                    checkbox_list.append(field.name)




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
        type_serializer = TypeSerializer(types, many=True)

        return JsonResponse(type_serializer.data, safe=False)

    elif request.method == 'POST':
        type_data = JSONParser().parse(request)
        type_serializer = TypeSerializer(data=type_data)

        if type_serializer.is_valid():
            type_serializer.save()

            return JsonResponse('Type Added', safe=False)

        return JsonResponse('Type Failed to Add', safe=False)

    elif request.method == 'PUT':
        type_data = JSONParser().parse(request)

        type_ = Type.objects.get(id=type_data['id'])
        type_serializer = TypeSerializer(type_, data=type_data)

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
            item_quantity = item.get('quantity')
            item_price = item.get('price')

            product = {'id': item_id, 'quantity': item_quantity, 'price': item_price}
            products_db.append(product)

        order_data.pop('items')
        products_db_str = json.dumps(products_db)
        order_data['products'] = products_db_str

        # TODO сделать парсер чтоб приводить телефон к общему виду
        # order_client_phone = order_data.pop('phone')
        # order_client_email = order_data.pop('email')
        # client = None

        # if order_client_phone or order_client_email:
        #     client = Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).first()
        #     print(Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).query)
        #
        # order_data['client'] = client.id

        order_serializer = OrderSerializer(data=order_data)

        if order_serializer.is_valid():
            order_serializer.save()

            return JsonResponse('Заказ оформлен', safe=False)

        return JsonResponse('Не удалось оформить заказ', safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['myFile']
    file_name = default_storage.save('products/' + file.name, file)

    return JsonResponse(file_name, safe=False)
