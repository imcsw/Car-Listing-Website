# Generated by Django 3.2.9 on 2021-11-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_carsimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsimage',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
