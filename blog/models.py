from django.db import models
from django.utils import timezone
from extensions.utils import django_jalali_converter





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


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['position']

    def __str__(self):
        return self.title

    objects = CatGoryManager()





class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d',' پیش نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image_post', verbose_name='تصویر')
    published = models.DateTimeField(default=timezone.now(), verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(CateGory, verbose_name='دسته بندی', related_name='post_category')
    number_post = models.IntegerField(unique=True, blank=True, null=True, default=1, verbose_name='شماره پست')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-published']


    def __str__(self):
        return self.title

    def j_published(self):
        return django_jalali_converter(self.published)
    j_published.short_description = 'زمان انتشار'

    def category_published(self):
        return self.category.filter(status=True)
    category_published.short_description = 'دسته بندی'


    objects = PostManager()






