# Generated by Django 4.0.2 on 2022-04-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayer_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='azan',
            field=models.DateTimeField(blank=True, help_text='Any changes to Azan time will be overwritten by the API', null=True),
        ),
    ]
