from email.policy import default

from django.db import models
from django.utils import timezone
from extensions.utils import django_jalali_converter
from django.utils.html import format_html
from account.models import User
from django.shortcuts import reverse
from django.contrib.contenttypes.fields import GenericRelation

from comment.models import Comment


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


class IPAddress(models.Model):
    ip = models.GenericIPAddressField(verbose_name='آی پی آدرس')

    class Meta:
        verbose_name = 'ی پی آدرس کاربران'
        verbose_name_plural = 'آی پی آدرس کاربران'

    def __str__(self):
        return self.ip


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
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through='PostHit', blank=True, null=True, related_name='hits')
    like_user = models.ManyToManyField(User, blank=True, null=True, verbose_name='پسندها')



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



class PostHit(models.Model):
    post = models.ForeignKey(Post, verbose_name='مقاله', on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, verbose_name='آی پی آدرس', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

class Slider(models.Model):
    title = models.CharField(max_length=200, default='slider', verbose_name='عنوان')
    posts_slider = models.ManyToManyField(Post, blank=True, null=True, related_name='slider_p', verbose_name='پست های اسلایدر')
    active = models.BooleanField(default=False, verbose_name='اسلایدر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title



class Hashtag(models.Model):
    post = models.ManyToManyField(Post, verbose_name='پست', related_name='tag_post')
    title = models.CharField(max_length=200, verbose_name='عنوان', default='خبر')
    slug = models.SlugField(max_length=100, default='news', unique=True, verbose_name='عنوان در url')
    hits = models.ManyToManyField(IPAddress, through='TagHit', blank=True, null=True, related_name='tag_hit')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'هشتگ'
        verbose_name_plural = 'هشتگ ها'


class TagHit(models.Model):
    post = models.ForeignKey(Hashtag, verbose_name='برچسب', on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, verbose_name='آی پی آدرس', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')