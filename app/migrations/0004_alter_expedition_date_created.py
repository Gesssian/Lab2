# Generated by Django 4.2.7 on 2024-09-14 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_expedition_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 14, 19, 24, 8, 895763, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]