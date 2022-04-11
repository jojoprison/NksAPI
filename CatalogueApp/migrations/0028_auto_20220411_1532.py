# Generated by Django 3.2.12 on 2022-04-11 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0027_auto_20220411_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_activity_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='boxes',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество ящиков'),
        ),
        migrations.AlterField(
            model_name='product',
            name='complete_with_drawers',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Комплектуется с типами тумб'),
        ),
        migrations.AlterField(
            model_name='product',
            name='depth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='disposition',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_layout',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Расположение дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_quantity',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='electrical_outlets',
            field=models.BooleanField(blank=True, null=True, verbose_name='Электрические розетки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='execution_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал исполнения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Особенности'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gas',
            field=models.BooleanField(blank=True, null=True, verbose_name='Газ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lamp',
            field=models.BooleanField(blank=True, max_length=50, null=True, verbose_name='Светильник'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mains_switch',
            field=models.BooleanField(blank=True, null=True, verbose_name='Автомат защиты электросети'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mods',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Модификации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='oven_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал рабочей камеры'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purpose',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Назначение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shelf_count',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество полок'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shelf_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал полок'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sink_count',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество моек'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sink_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Расположения мойки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sink_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал мойки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sink_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип мойки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='CatalogueApp.subtype', verbose_name='Подтип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tabletop_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал столешницы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='technology_rack',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Технологическая стойка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='titration_panel',
            field=models.BooleanField(blank=True, null=True, verbose_name='Табло титрования'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='CatalogueApp.type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='water',
            field=models.BooleanField(blank=True, null=True, verbose_name='Вода'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='subtype',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtypes', to='CatalogueApp.type', verbose_name='Тип'),
        ),
    ]
