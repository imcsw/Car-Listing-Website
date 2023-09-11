# Generated by Django 3.2.9 on 2021-11-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_testdrive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='testdrive',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='testdrive',
            name='lastName',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='testdrive',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]