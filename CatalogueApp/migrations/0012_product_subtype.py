# Generated by Django 3.2.12 on 2022-03-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0011_auto_20220325_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='CatalogueApp.subtype', verbose_name='Подтип'),
        ),
    ]
