# Generated by Django 2.1.4 on 2019-04-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20190422_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='sender',
            field=models.CharField(default='unknown', max_length=20),
        ),
    ]