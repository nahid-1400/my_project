# Generated by Django 4.0.4 on 2022-10-05 11:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_hashtag_hits_alter_post_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 5, 11, 16, 31, 848916, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
