from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ClientSerializer
from .models import Client
#
#
# class ClientDjoserViewSet(UserViewSet):
#     '''
#     Подключаем UserViewSet из модуля Djoser,
#     Который обрабатывает все необходимые запросы
#     '''
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
