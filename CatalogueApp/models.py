from django.db import models
from django.urls import reverse


class Product(models.Model):
    # общие поля для всех
    title = models.CharField(max_length=50, verbose_name='Название')
    series = models.CharField(max_length=40, verbose_name='Серия', null=True)
    article = models.CharField(max_length=40, verbose_name='Артикул', null=True)
    width = models.PositiveIntegerField(verbose_name='Ширина', null=True)
    height = models.PositiveIntegerField(verbose_name='Высота', null=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True)
    date_added = models.DateTimeField(verbose_name='Дата добавления', null=True)
    photo_file_name = models.CharField(max_length=100, null=True, verbose_name='Фото')
    # TODO досмотреть видос и сделать либо так
    # photo = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Фото')
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано', null=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, allow_unicode=True,
    #                         verbose_name='URL', null=True)
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип', null=True)

    # поля для столов обычных
    depth = models.IntegerField(verbose_name='Глубина', null=True)
    countertop_material = models.CharField(max_length=50, verbose_name='Материал столешницы', null=True)
    execution_material = models.CharField(max_length=50, verbose_name='Материал исполнения', null=True)
    purpose = models.CharField(max_length=50, verbose_name='Назначение', null=True)
    disposition = models.CharField(max_length=50, verbose_name='Расположение', null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
        # имеет важное значение для пагинации - в консоли будет алерт об этом

    def __str__(self):
        return self.title

    # 1. такой подход более предпочтительный в случае, когда есть связанные посты по
    # каким-либо индексам
    # 2. СОГЛАСНО КОНВЕНЦИИ, модули джанго используют этот метод в своей работе,
    # если он определен в модели (админка обращается для построения ссылок на модели)
    # 3. переходит по данной юрле, когда через форму добавляем новую запись
    # TODO добавить когда будем юзать слать
    # def get_absolute_url(self):
    #     return reverse('product', kwargs={'product_slug': self.slug})


class Type(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название', unique=True)

    # slug = models.SlugField(max_length=255, unique=True, db_index=True,
    #                         verbose_name='URL')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('type', kwargs={'type_slug': self.slug})

    class Meta:
        ordering = ['id']
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Тип изделий'


class TableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Столы')
        # TODO когда-нибудь протестить вот так
        # return super().get_queryset().filter(cat__name='Актрисы').select_related('type')


class Table(Product):
    objects = TableManager()

    class Meta:
        proxy = True
        # TODO может быть добавить ordering, надо потестить
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'


class CabinetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Шкаф')


class Cabinet(Product):
    objects = CabinetManager()

    class Meta:
        proxy = True
        verbose_name = 'Шкаф'
        verbose_name_plural = 'Шкафы'


class RackManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Стеллаж')


class Rack(Product):
    objects = RackManager()

    class Meta:
        proxy = True
        verbose_name = 'Стеллаж'
        verbose_name_plural = 'Стеллажи'

