# Generated by Django 3.2.12 on 2022-03-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0010_auto_20220325_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shelf_space',
        ),
        migrations.AddField(
            model_name='product',
            name='shelf_count',
            field=models.PositiveSmallIntegerField(max_length=50, null=True, verbose_name='Количество полок'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mains_switch',
            field=models.BooleanField(null=True, verbose_name='Автомат защиты электросети'),
        ),
    ]
