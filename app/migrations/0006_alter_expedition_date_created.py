# Generated by Django 4.2.7 on 2024-09-17 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_climber_options_alter_expedition_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 17, 19, 28, 59, 189789, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]