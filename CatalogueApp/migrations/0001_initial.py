# Generated by Django 3.2.12 on 2022-03-04 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, null=True, unique=True, verbose_name='Подтип изделия')),
            ],
            options={
                'verbose_name': 'Подтип изделия',
                'verbose_name_plural': 'Подтип изделий',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Название')),
                ('subtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CatalogueApp.subtype', verbose_name='Подтип')),
            ],
            options={
                'verbose_name': 'Тип изделия',
                'verbose_name_plural': 'Тип изделий',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('series', models.CharField(max_length=40, null=True, verbose_name='Серия')),
                ('article', models.CharField(max_length=40, null=True, verbose_name='Артикул')),
                ('width', models.PositiveIntegerField(null=True, verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(null=True, verbose_name='Высота')),
                ('depth', models.IntegerField(null=True, verbose_name='Глубина')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Цена')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('photo_file_name', models.CharField(max_length=100, null=True, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, null=True, verbose_name='Опубликовано')),
                ('execution_material', models.CharField(max_length=50, null=True, verbose_name='Материал исполнения')),
                ('purpose', models.CharField(max_length=50, null=True, verbose_name='Назначение')),
                ('oven_material', models.CharField(max_length=50, null=True, verbose_name='Материал рабочей камеры')),
                ('tabletop_material', models.CharField(max_length=50, verbose_name='Материал столешницы')),
                ('mains_switch', models.BooleanField(max_length=50, null=True, verbose_name='Автомат защиты электросети')),
                ('door_quantity', models.CharField(max_length=50, null=True, verbose_name='Количество дверец')),
                ('door_layout', models.CharField(max_length=50, null=True, verbose_name='Расположение дверец')),
                ('door_material', models.CharField(max_length=50, null=True, verbose_name='Материал дверец')),
                ('feature', models.CharField(max_length=50, null=True, verbose_name='Особенность')),
                ('disposition', models.CharField(max_length=50, null=True, verbose_name='Расположение')),
                ('drawer_type', models.CharField(max_length=50, null=True, verbose_name='Тип тумбы')),
                ('technology_rack', models.BooleanField(null=True, verbose_name='Технологическая стойка')),
                ('electrical_outlets', models.BooleanField(null=True, verbose_name='Электрическая розетка')),
                ('lamp', models.BooleanField(max_length=50, null=True, verbose_name='Светильник')),
                ('shelf_material', models.CharField(max_length=50, null=True, verbose_name='Материал полок')),
                ('shelf_space', models.CharField(max_length=50, null=True, verbose_name='Кол-во полок')),
                ('sink_material', models.CharField(max_length=50, null=True, verbose_name='Материал мойки')),
                ('sink_location', models.CharField(max_length=50, null=True, verbose_name='Расположения мойки')),
                ('mortise', models.CharField(max_length=50, null=True, verbose_name='Врезная мойка')),
                ('type_title', models.ForeignKey(db_column='type_title', on_delete=django.db.models.deletion.CASCADE, to='CatalogueApp.type', to_field='title', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Изделие',
                'verbose_name_plural': 'Изделия',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
            ],
            options={
                'verbose_name': 'Шкаф',
                'verbose_name_plural': 'Шкафы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CatalogueApp.product',),
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
            ],
            options={
                'verbose_name': 'Стул',
                'verbose_name_plural': 'Стулья',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CatalogueApp.product',),
        ),
        migrations.CreateModel(
            name='Drawer',
            fields=[
            ],
            options={
                'verbose_name': 'Тумба',
                'verbose_name_plural': 'Тумбы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CatalogueApp.product',),
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
            ],
            options={
                'verbose_name': 'Стеллаж',
                'verbose_name_plural': 'Стеллажи',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CatalogueApp.product',),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CatalogueApp.product',),
        ),
    ]
