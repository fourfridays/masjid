# Generated by Django 4.0.2 on 2022-04-19 04:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_alter_donatepage_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatepage',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 55, 57, 513451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 55, 57, 513437, tzinfo=utc)),
        ),
    ]
