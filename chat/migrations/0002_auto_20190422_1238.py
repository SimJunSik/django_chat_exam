# Generated by Django 2.1.4 on 2019-04-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test',
        ),
        migrations.AddField(
            model_name='test',
            name='room_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
