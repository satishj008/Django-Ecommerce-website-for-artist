# Generated by Django 3.2 on 2021-06-07 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210607_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
    ]