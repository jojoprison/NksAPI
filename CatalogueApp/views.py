import json

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
def product_filter_all_api(request):
    if request.method == 'GET':
        temp_filter_list = list(set(Product.objects.all().values_list('photo_file_name', flat=True)))
        temp_filter_list.sort()

        return JsonResponse(temp_filter_list, safe=False)


@csrf_exempt
def product_filter_api(request):
    if request.method == 'GET':
        photo = request.GET.get('photo', None)

        if photo == 'ALL':
            prods_by_photo = Product.objects.all()
        else:
            prods_by_photo = Product.objects.filter(photo_file_name=photo)

        print(prods_by_photo)
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
