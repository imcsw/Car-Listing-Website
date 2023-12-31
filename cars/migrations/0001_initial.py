# Generated by Django 3.2.9 on 2021-11-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carModel', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('dateAdded', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=25)),
                ('remarks', models.CharField(max_length=250)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
