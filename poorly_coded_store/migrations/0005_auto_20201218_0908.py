# Generated by Django 2.2 on 2020-12-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0004_auto_20201217_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]