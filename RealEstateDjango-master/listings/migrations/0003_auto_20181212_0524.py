# Generated by Django 2.1.4 on 2018-12-12 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_bathrooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bathrooms',
            new_name='bathroom',
        ),
    ]
