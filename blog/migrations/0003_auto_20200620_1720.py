# Generated by Django 3.0.7 on 2020-06-20 23:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200615_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 23, 20, 15, 570262, tzinfo=utc)),
        ),
    ]