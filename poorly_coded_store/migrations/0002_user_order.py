# Generated by Django 2.2 on 2020-12-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_spending', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
