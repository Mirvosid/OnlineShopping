# Generated by Django 4.2.6 on 2023-10-25 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_category_product_category_id_and_more'),
        ('shopcard', '0002_alter_shopcard_owner_alter_shopcard_payment'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='product',
        ),
        migrations.RemoveField(
            model_name='items',
            name='shopcard',
        ),
        migrations.AddField(
            model_name='items',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='items',
            name='shopcard_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopcard.shopcard'),
        ),
    ]
