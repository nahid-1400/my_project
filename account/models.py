from email.policy import default

import shortcuts as shortcuts
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='آدرس ایمیل')
    is_author = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    special_user = models.DateTimeField(default=timezone.now(), verbose_name='کاربر ویژه تا')
    profile_image = models.ImageField(upload_to='account/user-profile', blank=True, null=True, verbose_name='تصویر پروفایل')

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = 'وضعیت کاربر ویژه'

