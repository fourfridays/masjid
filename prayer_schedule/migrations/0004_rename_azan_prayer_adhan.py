# Generated by Django 4.0.2 on 2022-04-15 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prayer_schedule', '0003_alter_prayer_salah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prayer',
            old_name='azan',
            new_name='adhan',
        ),
    ]
