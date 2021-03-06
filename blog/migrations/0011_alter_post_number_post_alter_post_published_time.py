# Generated by Django 4.0.4 on 2022-04-23 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_options_remove_post_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_post',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='شماره پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 11, 4, 2, 130200, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
