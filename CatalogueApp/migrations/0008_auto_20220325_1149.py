# Generated by Django 3.2.12 on 2022-03-25 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0007_accessory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='disposition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='drawer_type',
        ),
        migrations.RemoveField(
            model_name='type',
            name='subtype',
        ),
        migrations.AddField(
            model_name='product',
            name='boxes',
            field=models.PositiveIntegerField(null=True, verbose_name='Ящики'),
        ),
        migrations.AddField(
            model_name='product',
            name='doors',
            field=models.CharField(max_length=50, null=True, verbose_name='Дверцы'),
        ),
        migrations.AddField(
            model_name='subtype',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtypes', to='CatalogueApp.type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_layout',
            field=models.CharField(max_length=50, null=True, verbose_name='Расположение дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_material',
            field=models.CharField(max_length=50, null=True, verbose_name='Материал дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='door_quantity',
            field=models.CharField(max_length=50, null=True, verbose_name='Количество дверей'),
        ),
        migrations.AlterField(
            model_name='product',
            name='electrical_outlets',
            field=models.BooleanField(null=True, verbose_name='Электрические розетки'),
        ),
    ]
