# Generated by Django 4.0.4 on 2022-08-27 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 10, 23, 33, 195888, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
