# Generated by Django 3.2.7 on 2021-10-25 20:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_activation_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 16, 2, 297552, tzinfo=utc)),
        ),
    ]
