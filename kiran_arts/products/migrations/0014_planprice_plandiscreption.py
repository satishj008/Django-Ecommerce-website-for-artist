# Generated by Django 3.2.6 on 2021-09-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_planprice_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='planprice',
            name='plandiscreption',
            field=models.TextField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
