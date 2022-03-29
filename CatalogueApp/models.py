import json

from django.db import models


class Product(models.Model):
    # общие поля для всех
    title = models.CharField(max_length=120, verbose_name='Название')
    series = models.CharField(max_length=40, verbose_name='Серия', null=True)
    article = models.CharField(max_length=40, verbose_name='Артикул', null=True)
    width = models.PositiveIntegerField(verbose_name='Ширина', null=True)
    height = models.PositiveIntegerField(verbose_name='Высота', null=True)
    depth = models.IntegerField(verbose_name='Глубина', null=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    # TODO придумать че делать с множественным фотками, пока добавляю первую
    photo_file_name = models.CharField(max_length=100, null=True, verbose_name='Фото')
    # TODO досмотреть видос и сделать либо так
    # photo = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Фото')
    description = models.CharField(max_length=2000, blank=True, verbose_name='Описание', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, allow_unicode=True,
    #                         verbose_name='URL', null=True)
    # TODO swappable
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, verbose_name='Тип',
                             related_name='products')
    subtype = models.ForeignKey('Subtype', on_delete=models.SET_NULL, null=True, verbose_name='Подтип',
                                related_name='products')

    # поля для столов обычных/моек/тумб
    execution_material = models.CharField(max_length=50, verbose_name='Материал исполнения', null=True)
    purpose = models.CharField(max_length=50, verbose_name='Назначение', null=True)
    # ///////// ^ ^ НАЗНАЧЕНИЕ и МАТЕРИАЛ ИСПОЛНЕНИЯ(29-30) + к классу "СТЕЛАЖИ" \\\\\\\\
    # 32 and 33 str for "ШКАФЫ"
    oven_material = models.CharField(max_length=50, verbose_name='Материал рабочей камеры', null=True)
    # ТУМБА 4
    tabletop_material = models.CharField(max_length=50, verbose_name='Материал столешницы')

    # [Справа, Слева] - для тумб,столов-моек [Справа, Слева, Наверху, Внизу] - для шкафов
    door_layout = models.CharField(max_length=50, verbose_name='Расположение дверей', null=True)
    # TODO подумать как фильтровать если 2 двери
    # TODO Choices
    # ТУМБЫ 1, 2 СТОЛЫ-МОЙКИ - 1,2
    door_quantity = models.PositiveSmallIntegerField(verbose_name='Количество дверей',
                                                     null=True)
    # шкафы, у тумб тот же, что и материал исполнения
    door_material = models.CharField(max_length=50, verbose_name='Материал дверей', null=True)
    # TODO мб для тумб сделать материал дверей как материал исполнения
    # [1, 2, 3, 4]
    boxes = models.PositiveIntegerField(verbose_name='Ящики', null=True)
    # TODO будет массивом для всякой непопулярной херни
    feature = models.CharField(max_length=50, verbose_name='Особенность', null=True)
    # СТОЛЫ-МОЙКИ
    disposition = models.CharField(max_length=50, verbose_name='Расположение', null=True)
    # СТОЛЫ 2
    # TODO мб убрать None отсутствует, хз как по логике это работает, надо посмотреть
    TECHNOLOGY_RACK = (
        (None, 'Отсутствует'),
        ('built_in', 'В комплекте'),
        ('separately', 'Отдельным заказом'),
    )
    technology_rack = models.CharField(choices=TECHNOLOGY_RACK, default=None, verbose_name='Технологическая стойка',
                                       null=True, max_length=30)
    # ШКАФЫ 2 (Эльвира сказала, пока не юзаем их), СТЕЛЛАЖИ 2
    shelf_material = models.CharField(max_length=50, verbose_name='Материал полок', null=True)
    # КОЛ-ВО ПОЛОК идут еще в "ШКАФЫ", "ТУМБЫ"
    shelf_count = models.PositiveSmallIntegerField(verbose_name='Количество полок', null=True)
    # СТОЛЫ-МОЙКИ
    sink_type = models.CharField(max_length=50, verbose_name='Тип мойки', null=True)
    sink_material = models.CharField(max_length=50, verbose_name='Материал мойки', null=True)
    sink_location = models.CharField(max_length=50, verbose_name='Расположения мойки', null=True)
    sink_count = models.PositiveSmallIntegerField(verbose_name='Количество моек', null=True)

    # ТУМБА 2
    mains_switch = models.BooleanField(verbose_name='Автомат защиты электросети', null=True)
    # СТОЛЫ 3
    electrical_outlets = models.BooleanField(verbose_name='Электрические розетки', null=True)
    water = models.BooleanField(verbose_name='Вода', null=True)
    gas = models.BooleanField(verbose_name='Газ', null=True)
    lamp = models.BooleanField(max_length=50, verbose_name='Светильник', null=True)
    # СТОЙКИ 1
    titration_panel = models.BooleanField(verbose_name='Табло титрования', null=True)
    # ТОЛЬКО СТОЛЫ 1
    # TODO сделать миграцию
    complete_with_drawers = models.CharField(max_length=50, verbose_name='Комплектуется с типами тумб',
                                             null=True)

    # модификации с Лабстола, там интересно сделано переключение между вариантами
    mods = models.CharField(max_length=1000, verbose_name='Модификации', null=True)

    # TODO дополнить базу этим, когда будет время
    # доп оборудование(ток для одной/растений)
    # поджопники  тип подж,материал исполнения назначение/ ножки на коле
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
    title = models.CharField(max_length=50, db_index=True, verbose_name='Подтип', unique=True,
                             null=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, verbose_name='Тип', null=True,
                             related_name='subtypes')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Подтип'
        verbose_name_plural = 'Подтип'


class TableManager(models.Manager):
    def get_queryset(self):
        # TODO придумать как будут отфильтровываться Product^. Время существительных)
        return super().get_queryset().filter(type__title='Стол')

        # select_related - загружает и данные из таблицы категории (ЖАДНАЯ ЗАГРУЗКА)
        # TODO протестить как работает type__title с двумя поджопниками (будет ли выводить вообще)
        # return super().get_queryset().select_related('type').filter(type__title='Стол')
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


# ПОКА НЕ ДЕЛАЕМ ЭЛЬВИРА СКАЗАЛА
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


class ChairManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Стул')


class Chair(Product):
    objects = ChairManager()

    class Meta:
        proxy = True
        verbose_name = 'Стул'
        verbose_name_plural = 'Стулья'


class DrawerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Тумба')


class Drawer(Product):
    objects = DrawerManager()

    class Meta:
        proxy = True
        verbose_name = 'Тумба'
        verbose_name_plural = 'Тумбы'


class StandManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Стойка')


class Stand(Product):
    objects = StandManager()

    class Meta:
        proxy = True
        verbose_name = 'Стойка'
        verbose_name_plural = 'Стойки'


class AccessoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Доп. оснащение')


class Accessory(Product):
    objects = DrawerManager()

    class Meta:
        proxy = True
        verbose_name = 'Доп. оснащение'
        verbose_name_plural = 'Доп. оснащение'


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя клиента')
    email = models.CharField(max_length=50, verbose_name='E-Mail клиента')
    first_activity_time = models.DateTimeField(auto_now_add=True, verbose_name='Когда зарегистрировался')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    # client = models.ForeignKey('Client', on_delete=models.SET_NULL, verbose_name='Клиент', null=True)
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона клиента')
    email = models.CharField(max_length=100, verbose_name='E-mail клиента')
    city = models.CharField(max_length=50, verbose_name='Город', null=True, blank=True)
    commentary = models.CharField(max_length=500, verbose_name='Комментарий к заказу', null=True,
                                  blank=True)
    price = models.IntegerField(verbose_name='Сумма заказа')
    delivery = models.CharField(max_length=50, null=True, blank=True, verbose_name='Вариант доставки')
    products = models.CharField(max_length=300, verbose_name='Товары')

    def __str__(self):
        return f'Заказ №{self.id}; тел. {self.phone} {self.name}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def __str__(self):
    #     return f'order_for_{self.client}#{self.id}'
    #
    # def set_products(self, products):
    #     self.products = json.dumps(products)
    #
    # def get_products(self):
    #     return json.loads(self.products)
