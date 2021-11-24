# Generated by Django 3.2.7 on 2021-10-27 12:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('selection', '0003_alter_floor_floor_levels'),
        ('offices', '0002_auto_20211025_2346'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('user', 'office', 'start_date', 'end_date')},
        ),
    ]