# Generated by Django 4.2.6 on 2023-10-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcard', '0003_alter_shopcard_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcard',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]