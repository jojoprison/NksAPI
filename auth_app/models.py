from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    '''
    Расширяем стандартного User'а для работы с Djoser
    '''
    name = models.CharField(max_length=50, verbose_name='Имя клиента')
    email = models.CharField(max_length=50, verbose_name='E-Mail клиента', unique=True)
    first_activity_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', unique=True)
    password = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
