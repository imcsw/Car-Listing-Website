# Generated by Django 3.2.9 on 2021-12-11 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_remove_carsimage_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='date',
        ),
    ]
