# Generated by Django 4.1 on 2022-08-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admingrafic',
            name='decimalx',
            field=models.CharField(max_length=200, verbose_name='ось x'),
        ),
        migrations.AlterField(
            model_name='admingrafic',
            name='decimaly',
            field=models.CharField(max_length=200, verbose_name='ось y'),
        ),
    ]
