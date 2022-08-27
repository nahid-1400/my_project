# Generated by Django 4.0.4 on 2022-07-25 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_special',
        ),
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 25, 12, 44, 39, 479360, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]