# Generated by Django 4.0.4 on 2022-09-08 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 8, 11, 59, 58, 33830, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]
