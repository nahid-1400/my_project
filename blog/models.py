from django.db import models
from django.utils import timezone
from extensions.utils import django_jalali_converter
from django.utils.html import format_html
from account.models import User
from django.shortcuts import reverse


class CatGoryManager(models.Manager):
    def category_status(self, slug):
        return self.filter(status=True, slug=slug)

    def category_active(self):
        return self.filter(status=True)




class CateGory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='عنوان دسته بندی در url')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='children', verbose_name='والد')
    status = models.BooleanField(default=True, verbose_name='این دسته بندی  نمایش داده شوند؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    image = models.ImageField(upload_to='category', default='category/defualt.jpg', verbose_name='تصویر دسته بندی')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

    objects = CatGoryManager()





class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Post(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    STATUS_CHOICES = (
        ('d', ' پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'در حال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image_post', verbose_name='تصویر')
    published_time = models.DateTimeField(default=timezone.now(), verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(CateGory, verbose_name='دسته بندی', related_name='post_category')
    number_post = models.IntegerField(unique=True, blank=True, null=True, verbose_name='شماره پست')
    is_special = models.BooleanField(default=False, verbose_name='مقاله ویژه')


    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-published_time']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:home')

    def j_published(self):
        return django_jalali_converter(self.published_time)
    j_published.short_description = 'زمان انتشار'


    def image_tag(self):
        return format_html("<img height=100px width=110px style='border-radius: 5px;'  src='{}'>".format(self.image.url))
    image_tag.short_description = 'تصویر'
    objects = PostManager()

    def category_to_str(self):
        return ', '.join([category.title for category in self.category.category_active()])
    category_to_str.short_description = 'دسته بندی'





