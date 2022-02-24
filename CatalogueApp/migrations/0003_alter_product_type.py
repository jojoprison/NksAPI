# Generated by Django 3.2.12 on 2022-02-23 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0002_alter_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='CatalogueApp.type', verbose_name='Тип'),
        ),
    ]
