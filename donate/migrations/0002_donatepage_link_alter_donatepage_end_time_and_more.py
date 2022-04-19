# Generated by Django 4.0.2 on 2022-04-19 04:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatepage',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 6, 8, 19599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 6, 8, 19587, tzinfo=utc)),
        ),
    ]