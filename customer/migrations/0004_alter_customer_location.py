# Generated by Django 4.2.6 on 2023-10-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
