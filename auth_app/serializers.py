from djoser.serializers import UserSerializer, UserCreateSerializer

from .models import Client


class ClientSerializer(UserSerializer):
    '''
    Сериализатор для вывода информации о пользователе
    '''
    class Meta:
        model = Client
        fields = (
            'id', 'email',
            'name', 'first_activity_time',
            'phone'
        )


class ClientCreateSerializer(UserCreateSerializer):
    '''
    Сериализатор для создания пользователя
    '''
    class Meta:
        model = Client
        fields = (
            'id', 'email', "username",
            'name', 'first_activity_time',
            'phone', 'password'
        )