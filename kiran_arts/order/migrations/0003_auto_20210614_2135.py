# Generated by Django 3.2 on 2021-06-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210613_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service_price',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='ship_address',
            field=models.TextField(max_length=1000),
        ),
    ]
