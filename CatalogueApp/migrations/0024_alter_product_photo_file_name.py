# Generated by Django 3.2.12 on 2022-03-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0023_product_is_correct_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_file_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Фото'),
        ),
    ]
