# Generated by Django 4.0.4 on 2022-08-01 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='آدرس ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 1, 10, 14, 1, 289073, tzinfo=utc), verbose_name='کاربر ویژه تا'),
        ),
    ]
