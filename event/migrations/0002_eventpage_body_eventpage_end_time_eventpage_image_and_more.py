# Generated by Django 4.0.2 on 2022-04-18 06:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='body',
            field=wagtail.core.fields.StreamField([('description', wagtail.core.blocks.RichTextBlock())], default=''),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 1, 41, 30, 268343)),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='2400X858px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 1, 41, 30, 268330)),
        ),
    ]
