# Generated by Django 3.2.9 on 2021-11-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20211126_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
