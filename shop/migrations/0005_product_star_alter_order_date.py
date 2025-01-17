# Generated by Django 5.0.7 on 2024-07-24 19:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 22, 54, 58, 157418)),
        ),
    ]
