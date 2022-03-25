import json
import operator
from functools import reduce

from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CatalogueApp.models import Product, Type, Client
from CatalogueApp.serializers import ProductSerializer, TypeSerializer,\
    FilterSerializer, ClientSerializer, OrderSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def product_api(request, product_id=0):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)

        return JsonResponse(product_serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)

        if product_serializer.is_valid():
            product_serializer.save()

            return JsonResponse('Product Added', safe=False)

        return JsonResponse('Product Failed to Add', safe=False)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)

        product = Product.objects.get(id=product_data['id'])
        product_serializer = ProductSerializer(product, data=product_data)

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
        product_serializer = ProductSerializer(product)

        return JsonResponse(product_serializer.data, safe=False)


@csrf_exempt
def product_filter_all_api(request):
    if request.method == 'GET':
        photo_list = list(set(Product.objects.all().values_list('photo_file_name', flat=True)))
        photo_list.sort()
        print(photo_list)

        price_list = list(set(Product.objects.all().exclude(price=None).values_list('price', flat=True)))
        print(price_list)
        price_list.sort()

        type_list = list(set(Product.objects.all().values_list('type__title', flat=True)))
        type_list.sort()

        filter_variant_list = {
            'select': [
                {'product_prop': 'type',
                 # TODO мб как то можно verbose_name засунуть из модельки сюда
                 'name': 'Тип',
                 'values': type_list},
                {'product_prop': 'price',
                 'name': 'Цена',
                 'values': price_list},
                {'product_prop': 'photo_file_name',
                 'name': 'Фото',
                 'values': photo_list},
                {'product_prop': 'width',
                 'name': 'Ширина',
                 'values': photo_list},
                {'product_prop': 'photo_file_name',
                 'name': 'Фото',
                 'values': photo_list},
                {'product_prop': 'photo_file_name',
                 'name': 'Фото',
                 'values': photo_list},
                {'product_prop': 'photo_file_name',
                 'name': 'Фото',
                 'values': photo_list},
            ],
            'checkbox': ['is_published', 'lol', 'temp']
        }

        print(filter_variant_list)

        return JsonResponse(filter_variant_list, safe=False)


@csrf_exempt
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

        print(filter_kwargs)

        # TODO заменить проверки вот тут
        if request.GET.get('photo', None) == 'ALL':
            prods_by_photo = Product.objects.all()
        else:
            if filter_kwargs:
                prods_by_photo = Product.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                prods_by_photo = Product.objects.all()

        product_serializer = ProductSerializer(prods_by_photo, many=True)

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
        # TODO сделать парсер чтоб приводить телефон к общему виду
        order_client_phone = order_data.pop('phone')
        order_client_email = order_data.pop('email')
        client = None

        if order_client_phone or order_client_email:
            client = Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).first()
            print(Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).query)

        order_data['client'] = client.id
        order_data['products'] = json.dumps(order_data.get('products'))

        order_serializer = OrderSerializer(data=order_data)

        if order_serializer.is_valid():
            order_serializer.save()

        return JsonResponse('Заказ записан епта', safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['myFile']
    file_name = default_storage.save('products/' + file.name, file)

    return JsonResponse(file_name, safe=False)
