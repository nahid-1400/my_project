# Generated by Django 4.0.4 on 2022-09-27 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 12, 2, 12, 135862, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]