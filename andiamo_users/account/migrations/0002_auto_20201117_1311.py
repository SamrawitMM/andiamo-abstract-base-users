# Generated by Django 3.1.2 on 2020-11-17 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='current_latitude',
            field=models.FloatField(default=None, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='current_longitude',
            field=models.FloatField(default=None, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='previous_latitude',
            field=models.FloatField(default=None, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='previous_longitude',
            field=models.FloatField(default=None, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]