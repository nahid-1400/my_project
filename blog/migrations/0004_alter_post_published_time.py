# Generated by Django 4.0.4 on 2022-08-01 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_special_alter_post_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 1, 10, 14, 1, 294073, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
