# Generated by Django 3.2.12 on 2022-03-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0015_auto_20220325_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mods',
            field=models.CharField(max_length=150, null=True, verbose_name='Модификации'),
        ),
    ]
