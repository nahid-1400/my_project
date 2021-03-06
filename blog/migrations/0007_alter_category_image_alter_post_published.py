# Generated by Django 4.0.4 on 2022-04-13 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_image_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category/defualt.jpg', upload_to='category', verbose_name='تصویر دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 12, 42, 2, 784150, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
