# Generated by Django 3.2.12 on 2022-04-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0025_auto_20220404_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.CharField(max_length=10000, verbose_name='Товары'),
        ),
    ]
