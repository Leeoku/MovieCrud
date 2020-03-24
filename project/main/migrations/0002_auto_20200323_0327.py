# Generated by Django 3.0.4 on 2020-03-23 03:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieentry',
            name='alt_title_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='alt_title_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='count',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='director',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='dvd_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='form_field',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='language',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='movieentry',
            name='spec',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='year',
            field=models.IntegerField(blank=True, default=1900, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
