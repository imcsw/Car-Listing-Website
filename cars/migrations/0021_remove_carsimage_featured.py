# Generated by Django 3.2.9 on 2021-12-10 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_auto_20211210_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsimage',
            name='featured',
        ),
    ]
