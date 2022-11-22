from django.db import models
from account.models import User

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='کاربر')
    subject = models.CharField(max_length=200, verbose_name='عنوان')
    message_text = models.TextField(verbose_name='پیغام')

    class Meta:
        verbose_name = 'تیکت کاربر'
        verbose_name_plural = 'تیکت کاربران'

    def __str__(self):
        return self.subject
