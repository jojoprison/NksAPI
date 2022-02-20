from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CatalogueApp.models import Table
from CatalogueApp.serializers import TableSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def table_api(request, table_id=0):
    if request.method == 'GET':
        tables = Table.objects.all()
        table_serializer = TableSerializer(tables, many=True)

        return JsonResponse(table_serializer.data, safe=False)

    elif request.method == 'POST':
        table_data = JSONParser().parse(request)
        table_serializer = TableSerializer(data=table_data)

        if table_serializer.is_valid():
            table_serializer.save()

            return JsonResponse('Added', safe=False)

        return JsonResponse('Failed to Add', safe=False)

    elif request.method == 'PUT':
        table_data = JSONParser().parse(request)

        table = Table.objects.get(id=table_data['id'])
        table_serializer = TableSerializer(table, data=table_data)

        if table_serializer.is_valid():
            table_serializer.save()

            return JsonResponse('Updated', safe=False)

        return JsonResponse('Failed to Update', safe=False)

    elif request.method == 'DELETE':
        table = Table.objects.get(id=table_id)
        table.delete()

        return JsonResponse('Deleted', safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
