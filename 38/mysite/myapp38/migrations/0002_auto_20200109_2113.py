# Generated by Django 2.2 on 2020-01-09 19:13

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp38', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='lim_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=datetime.datetime(2020, 1, 10, 19, 13, 48, 848484, tzinfo=utc)),
        ),
    ]
