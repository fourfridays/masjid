# Generated by Django 4.0.2 on 2022-04-19 05:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('donate', '0007_alter_donateindexpage_hero_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateindexpage',
            name='hero_heading',
            field=models.CharField(blank=True, help_text='40 character limit.', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='donateindexpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='2400X858px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 5, 17, 26, 578302, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='hero_image',
            field=models.ForeignKey(help_text='2400X858px', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='images.customimage'),
        ),
        migrations.AlterField(
            model_name='donatepage',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 5, 17, 26, 578290, tzinfo=utc)),
        ),
    ]
