# Generated by Django 4.0.4 on 2022-10-05 11:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 5, 11, 16, 31, 731909, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]
