# Generated by Django 4.2.6 on 2023-10-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_items_product_remove_items_shopcard_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='sell_date',
            field=models.DateTimeField(),
        ),
    ]
