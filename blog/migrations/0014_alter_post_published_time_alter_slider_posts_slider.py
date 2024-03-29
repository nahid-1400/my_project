# Generated by Django 4.0.4 on 2022-09-27 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_slider_title_alter_post_published_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 12, 2, 12, 210867, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='posts_slider',
            field=models.ManyToManyField(blank=True, max_length=6, null=True, related_name='slider_p', to='blog.post', verbose_name='پست های اسلایدر'),
        ),
    ]
