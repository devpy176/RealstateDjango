# Generated by Django 2.1.4 on 2018-12-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20181212_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(default='Pune', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='Maharashtra', max_length=200),
        ),
    ]
