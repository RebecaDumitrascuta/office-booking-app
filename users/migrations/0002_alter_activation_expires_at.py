# Generated by Django 3.2.7 on 2021-10-19 16:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 16, 52, 20, 209896, tzinfo=utc)),
        ),
    ]
