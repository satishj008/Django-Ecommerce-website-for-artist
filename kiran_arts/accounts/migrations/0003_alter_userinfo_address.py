# Generated by Django 3.2 on 2021-06-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinfo_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(max_length=1000),
        ),
    ]
