# Generated by Django 4.0.2 on 2022-04-16 15:13

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prayer_schedule', '0006_prayerscheduleapisetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerScheduleExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', wagtail.core.fields.RichTextField()),
            ],
        ),
    ]
