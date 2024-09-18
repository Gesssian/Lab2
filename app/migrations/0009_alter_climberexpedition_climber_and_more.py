# Generated by Django 4.2.7 on 2024-09-18 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_expedition_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climberexpedition',
            name='climber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.climber', verbose_name='Альпинист'),
        ),
        migrations.AlterField(
            model_name='climberexpedition',
            name='expedition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.expedition', verbose_name='Экспедиция'),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 18, 5, 13, 48, 686439, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterUniqueTogether(
            name='climberexpedition',
            unique_together={('climber', 'expedition')},
        ),
        migrations.AlterModelTable(
            name='climberexpedition',
            table='climber_expeditions',
        ),
        migrations.RemoveField(
            model_name='climberexpedition',
            name='id',
        ),
    ]