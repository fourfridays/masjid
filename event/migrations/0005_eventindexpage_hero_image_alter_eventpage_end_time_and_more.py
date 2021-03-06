# Generated by Django 4.0.2 on 2022-04-18 07:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('event', '0004_alter_eventpage_end_time_alter_eventpage_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindexpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='2400X858px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 7, 21, 42, 745907, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 7, 21, 42, 745894, tzinfo=utc)),
        ),
    ]
