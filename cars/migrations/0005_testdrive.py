# Generated by Django 3.2.9 on 2021-11-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_cars_shortdesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=25)),
                ('date', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cars')),
            ],
        ),
    ]
