# Generated by Django 3.2 on 2021-06-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='contact',
            field=models.CharField(default=7030336891, max_length=13),
            preserve_default=False,
        ),
    ]
