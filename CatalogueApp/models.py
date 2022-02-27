from django.db import models
from django.urls import reverse


class Product(models.Model):
    # общие поля для всех
    title = models.CharField(max_length=50, verbose_name='Название')
    series = models.CharField(max_length=40, verbose_name='Серия', null=True)
    article = models.CharField(max_length=40, verbose_name='Артикул', null=True)
    width = models.PositiveIntegerField(verbose_name='Ширина', null=True)
    height = models.PositiveIntegerField(verbose_name='Высота', null=True)
    depth = models.IntegerField(verbose_name='Глубина', null=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True)
    date_added = models.DateTimeField(verbose_name='Дата добавления', null=True, auto_now_add=True)
    photo_file_name = models.CharField(max_length=100, null=True, verbose_name='Фото')
    # TODO досмотреть видос и сделать либо так
    # photo = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Фото')
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано', null=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, allow_unicode=True,
    #                         verbose_name='URL', null=True)
    # TODO swappable
    type = models.ForeignKey('Type', to_field='title', on_delete=models.SET_DEFAULT, default='Любой',
                             verbose_name='Тип', db_column='type_title')


    # поля для столов обычных/ для моек
    execution_material = models.CharField(max_length=50, verbose_name='Материал исполнения', null=True)
    purpose = models.CharField(max_length=50, verbose_name='Назначение', null=True)
    # ///////// ^ ^ НАЗНАЧЕНИЕ и МАТЕРИАЛ ИСПОЛНЕНИЯ(28-29) + к классу "СТЕЛАЖИ" \\\\\\\\
    # 32 and 33 str only for "ШКАФЫ"
    oven_material = models.CharField(max_length=50, verbose_name='Материал рабочей камеры', null=True)
    tabletop_material = models.CharField(max_length=50, verbose_name='Материал столешницы', null=True)
    mains_switch = models.BooleanField(max_length=50, verbose_name='Автомат защиты электросети', null=True)
    door_quantity = models.CharField(verbose_name='Количество дверец', null=True)
    door_layout = models.CharField(verbose_name='Расположение дверец', null=True)
    door_material = models.CharField(verbose_name='Материал дверец', null=True)
    feature = models.CharField(max_length=50, verbose_name='Особенность', null=True)
    # /////////// Тип "ТУМБА" (Кол-во и расположение дверец) , тип "ШКАФЫ" - все(7 верхних)
    disposition = models.CharField(max_length=50, verbose_name='Расположение', null=True)
    drawer_type = models.CharField(max_length=50, verbose_name='Тип тумбы', null=True)
    # ///////// ^ ^ ТИП ТУМБЫ и РАСПОЛОЖЕНИЕ + к классу "ТУМБЫ" ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ \\\\\\\\\
    technology_rack = models.BooleanField(verbose_name='Технологическая стойка', null=True)
    electrical_outlets = models.BooleanField(verbose_name='Электрическая розетка', null=True)
    lamp = models.BooleanField(max_length=50, verbose_name='Светильник', null=True)
    # =====================  ИДУТ "ТУМБЫ" (2 верхних стр(43-44)) и "ШКАФЫ"(2 нижних(42-43)) ^ ^ ^ ^ ^ ^ ^ ^ ^
    shelf_material = models.CharField(verbose_name='Материал полок', null=True)
    shelf_space = models.CharField(verbose_name='Кол-во полок', null=True)
    # ///////// ^ ^ КОЛ-ВО ПОЛОК  ^ ^ ^ ^ ^ ^ идут еще в "ШКАФЫ", "ТУМБЫ", "СТЕЛЛАЖИ"(2 строки сверху)
    #
    # для столов-моек(плюсом,only!):
    sink_material = models.CharField(max_length=50, verbose_name='Материал мойки', null=True)
    sink_location = models.CharField(max_length=50, verbose_name='Расположения мойки', null=True)
    mortise = models.CharField(verbose_name='Врезная мойка', null=True)

     # TODO если оставляем хуйню снизу(4 строки) , то добавить по ним инфу
    # доп оборудование(ток для одной/растений)
    # поджопники  тип подж,материал исполнения назначение/ ножки на коле
    # доп оснащения : стойка тип стойки розетки(bool) расположение вода? газ?
    # бутыли. канистры (2 катег) материал назначение объем ручка(bool) кран(bool)

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
    subtype = models.ForeignKey('Subtype', on_delete=models.SET_NULL, verbose_name='Подтип', null=True)
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


class Subtype(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название', unique=True,
                             null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Подтип изделия'
        verbose_name_plural = 'Подтип изделий'


class TableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Столы')
        # TODO придумать как будут отфильтровываться Product^. Время существительных)
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
        return super().get_queryset().filter(type__title='Шкафы')


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


class ChairManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Стул')


class Chair(Product):
    objects = ChairManager()

    class Meta:
        proxy = True
        verbose_name = 'Стул'
        verbose_name_plural = 'Стулья'


class DrawerManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Тумба')


class Drawer(Product):
    objects = DrawerManager()

    class Meta:
        proxy = True
        verbose_name = 'Тумба'
        verbose_name_plural = 'Тумбы'
