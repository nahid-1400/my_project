# Generated by Django 4.0.4 on 2022-05-10 16:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_author_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 16, 32, 24, 296786, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]
